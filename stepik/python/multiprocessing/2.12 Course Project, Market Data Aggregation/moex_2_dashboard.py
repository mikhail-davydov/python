import concurrent.futures
import logging
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime
from get_investment import get_investment

logging.basicConfig(
    level=logging.INFO,
    filename="log_dashboard.txt",
    format="{processName}, {threadName}, {asctime}, {message}",
    style="{",
)


def process_ticker(ticker, ticker_share, start_date, end_date, investment_sum):
    try:
        result_df = get_investment(
            ticker=ticker,
            ticker_share=ticker_share,
            strategy_start_date=datetime.combine(start_date, datetime.min.time()),
            strategy_end_date=datetime.combine(end_date, datetime.min.time()),
            investment_sum=investment_sum,
        )
        result_df["ticker"] = ticker
        logging.info(f"Processed ticker: {ticker}")
        return result_df
    except Exception as e:
        return {"error": str(e), "ticker": ticker}


def main():
    st.set_page_config(layout="wide")
    st.title("Дашборд по инвестициям")
    st.sidebar.header("Параметры стратегии")

    available_tickers = []
    for file in os.listdir("output"):
        if file.endswith("_history.csv"):
            ticker = file.split("_")[0]
            if os.path.exists(f"output/{ticker}_dividends.csv"):
                available_tickers.append(ticker)

    default_tickers = [
        "SBER",
        "SBERP",
        "LKOH",
        "NVTK",
        "SIBN",
        "GMKN",
        "SNGS",
        "SNGSP",
        "PLZL",
        "CHMF",
        "PHOR",
        "AKRN",
        "YNDX",
        "MGNT",
        "MOEX",
    ]
    default_tickers = [t for t in default_tickers if t in available_tickers]

    ticker_names = {
        "SBER": "Сбербанк",
        "SBERP": "Сбербанк, привилегированные акции",
        "LKOH": "Лукойл",
        "NVTK": "Новатэк",
        "SIBN": "Газпромнефть",
        "GMKN": "ГМК Норильский никель",
        "SNGS": "Сургутнефтегаз",
        "SNGSP": "Сургутнефтегаз, привилегированные акции",
        "PLZL": "Полюс золото",
        "CHMF": "Северсталь",
        "PHOR": "ФосАгро",
        "AKRN": "Акрон",
        "YNDX": "Яндекс",
        "MGNT": "Магнит",
        "MOEX": "Московская биржа",
    }

    selected_tickers = st.sidebar.multiselect(
        "Выберите тикеры",
        options=available_tickers,
        default=default_tickers[:5],
        format_func=lambda x: x + f" ({ticker_names[x]})",
    )

    min_date = datetime(2010, 1, 1)
    max_date = datetime.today()

    start_date = st.sidebar.date_input(
        "Начальная дата", value=datetime(2023, 1, 1), min_value=min_date, max_value=max_date,
    )

    end_date = st.sidebar.date_input(
        "Конечная дата", value=max_date, min_value=start_date, max_value=max_date,
    )

    investment_sum = st.sidebar.number_input(
        "Ежемесячный инвестиционный объем",
        min_value=1000,
        max_value=1000000,
        value=10000,
        step=1000,
    )

    equal_weight = st.sidebar.checkbox("Равномерное распределение", value=True)

    ticker_weights = {}
    if not equal_weight and selected_tickers:
        st.sidebar.subheader("Веса тикеров")
        total_weight = 0

        for ticker in selected_tickers:
            weight = st.sidebar.slider(
                f"Вес {ticker}",
                min_value=0.0,
                max_value=1.0,
                value=1.0 / len(selected_tickers),
                step=0.01,
                key=f"weight_{ticker}",
            )
            ticker_weights[ticker] = weight
            total_weight += weight

        if total_weight != 1.0:
            st.sidebar.warning(f"Сумма весов равна {total_weight:.2f}, будет нормализована до 1.0")
            for ticker in ticker_weights:
                ticker_weights[ticker] /= total_weight
    else:
        for ticker in selected_tickers:
            ticker_weights[ticker] = 1.0 / len(selected_tickers) if selected_tickers else 0

    calculate_button = st.sidebar.button("Рассчитать инвестиционную стратегию")

    if not selected_tickers:
        st.warning("Пожалуйста, выберите хотя бы один тикер из боковой панели.")
    elif calculate_button:
        with st.spinner("Расчет инвестиционной стратегии..."):
            try:
                process_args = []
                for ticker in selected_tickers:
                    ticker_share = ticker_weights[ticker]
                    process_args.append(
                        (ticker, ticker_share, start_date, end_date, investment_sum),
                    )

                results = []
                failed_tickers = []

                progress_bar = st.progress(0)
                status_text = st.empty()

                with concurrent.futures.ProcessPoolExecutor() as executor:
                    future_to_ticker = {
                        executor.submit(process_ticker, *args): args[0] for args in process_args
                    }

                    completed = 0
                    for future in concurrent.futures.as_completed(future_to_ticker):
                        ticker = future_to_ticker[future]
                        try:
                            result = future.result()
                            if isinstance(result, dict) and "error" in result:
                                failed_tickers.append((result["ticker"], result["error"]))
                            else:
                                results.append(result)
                        except Exception as e:
                            failed_tickers.append((ticker, str(e)))

                        completed += 1
                        progress_bar.progress(completed / len(process_args))
                        status_text.text(f"Processed {completed}/{len(process_args)} tickers")

                progress_bar.empty()
                status_text.empty()

                if failed_tickers:
                    st.error(f"Failed to process {len(failed_tickers)} ticker(s):")
                    for ticker, error in failed_tickers:
                        st.error(f"{ticker}: {error}")

                if results:
                    final_df = results[0][["date", "investment"]].copy()
                    final_df["total_value"] = 0

                    for result in results:
                        ticker = result["ticker"].iloc[0]
                        final_df[f"{ticker}_value"] = result["ticker_value"]
                        final_df["total_value"] += result["ticker_value"]

                    final_df["cumulative_investment"] = final_df["investment"].fillna(0).cumsum()

                    final_df["profit_loss"] = (
                            final_df["total_value"] - final_df["cumulative_investment"]
                    )
                    final_df["profit_loss_pct"] = (
                                                          final_df["profit_loss"] / final_df["cumulative_investment"]
                                                  ) * 100

                    col1, col2, col3, col4 = st.columns(4)

                    total_invested = final_df["cumulative_investment"].iloc[-1]
                    final_value = final_df["total_value"].iloc[-1]
                    profit_loss = final_df["profit_loss"].iloc[-1]
                    profit_loss_pct = final_df["profit_loss_pct"].iloc[-1]

                    col1.metric("Общая инвестиция", f"{total_invested:,.2f}")
                    col2.metric("Текущая стоимость", f"{final_value:,.2f}")
                    col3.metric("Прибыль/Убыток", f"{profit_loss:,.2f}")
                    col4.metric("Возврат %", f"{profit_loss_pct:.2f}%")

                    (
                        tab1,
                        tab2,
                    ) = st.tabs(["Рост стоимости портфеля", "Стоимость тикеров во времени"])

                    with tab1:
                        fig = go.Figure()
                        fig.add_trace(
                            go.Scatter(
                                x=final_df["date"],
                                y=final_df["total_value"],
                                name="Общая стоимость портфеля",
                                mode="lines",
                            ),
                        )
                        fig.add_trace(
                            go.Scatter(
                                x=final_df["date"],
                                y=final_df["cumulative_investment"],
                                name="Общая инвестиция",
                                mode="lines",
                            ),
                        )
                        fig.update_layout(
                            title="Рост стоимости портфеля во времени",
                            xaxis_title="Дата",
                            yaxis_title="Стоимость",
                        )
                        st.plotly_chart(fig, use_container_width=True)

                    with tab2:
                        fig3 = go.Figure()

                        for ticker in [r["ticker"].iloc[0] for r in results]:
                            fig3.add_trace(
                                go.Scatter(
                                    x=final_df["date"],
                                    y=final_df[f"{ticker}_value"],
                                    mode="lines",
                                    name=ticker,
                                ),
                            )

                        fig3.update_layout(
                            title="Стоимость тикеров во времени",
                            xaxis_title="Дата",
                            yaxis_title="Стоимость",
                            legend=dict(x=0.01, y=0.99),
                            height=500,
                        )
                        st.plotly_chart(fig3, use_container_width=True)

                        processed_tickers = [r["ticker"].iloc[0] for r in results]

                        plot_data = pd.DataFrame()
                        plot_data["date"] = final_df["date"]

                        for ticker in processed_tickers:
                            plot_data[ticker] = final_df[f"{ticker}_value"]

                        plot_data_melted = pd.melt(
                            plot_data,
                            id_vars=["date"],
                            value_vars=processed_tickers,
                            var_name="Ticker",
                            value_name="Value",
                        )

                        fig4 = px.area(
                            plot_data_melted,
                            x="date",
                            y="Value",
                            color="Ticker",
                            title="Состав портфеля во времени",
                        )

                        fig4.update_layout(
                            xaxis_title="Дата",
                            yaxis_title="Стоимость",
                            legend_title="Тикер",
                            height=500,
                        )

                        st.plotly_chart(fig4, use_container_width=True)

                else:
                    st.error(
                        "Не были рассчитаны результаты. Пожалуйста, проверьте ваши входные данные.",
                    )

            except Exception as e:
                st.error(f"An error occurred during calculation: {str(e)}")
    else:
        st.info(
            "Выберите тикеры и параметры стратегии в боковой панели, затем нажмите 'Рассчитать инвестиционную стратегию' для просмотра результатов.",
        )

        st.markdown(
            """
        ## Как использовать этот дашборд
        
        1. Выберите один или несколько тикеров из боковой панели
        2. Установите начальную и конечную даты стратегии
        3. Введите ежемесячный инвестиционный объем
        4. Выберите равномерное распределение или настройте индивидуальные веса
        5. Нажмите 'Рассчитать инвестиционную стратегию' для просмотра результатов
        
        Дашборд рассчитает, как ваши инвестиции могли бы выполниться за выбранный период времени,
        и отобразит различные графики и метрики для анализа результатов.
        """,
        )


if __name__ == "__main__":
    main()
