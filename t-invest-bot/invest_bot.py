from t_tech.invest import Client, GetAssetFundamentalsRequest
from t_tech.invest.constants import INVEST_GRPC_API_SANDBOX, INVEST_GRPC_API
from t_tech.invest.schemas import GetMarketValuesRequest, MarketValueType, Share

import logger
import utils
from model import Settings

log = logger.get(__name__)


def filtered_data(share: Share):
    return share.buy_available_flag and share.sell_available_flag and share.name == "ВК"


def invest_bot(settings: Settings):
    token = settings.token.sandbox if settings.sandbox_mode else settings.token.read
    target = INVEST_GRPC_API_SANDBOX if settings.sandbox_mode else INVEST_GRPC_API
    log.debug(f"token: {token}, target: {target}")

    with get_client(target, token) as client:
        log.info(client.users.get_accounts())
        log.info("accounts: {}".format(client.users.get_accounts()))
        log.info("info: {}".format(client.users.get_info()))

    shares = get_shares(get_client(target, token))

    asset_ids = [share.asset_uid for share in shares]
    get_fundamentals(get_client(target, token), asset_ids)

    instrument_ids = [share.uid for share in shares]
    get_market_values(get_client(target, token), instrument_ids)

    # df_fundamentals = pd.DataFrame(fundamentals)
    # log.debug(f"df_fundamentals:\n{df_fundamentals[["ebitda_ttm", "net_debt_to_ebitda", "current_ratio_mrq"]]}")


def get_client(target, token):
    return Client(token=token, target=target)


def get_market_values(client, instrument_ids):
    with client as client:
        market_values = client.market_data.get_market_values(
            request=GetMarketValuesRequest(
                instrument_id=instrument_ids,
                values=[
                    MarketValueType.INSTRUMENT_VALUE_LAST_PRICE,
                    MarketValueType.INSTRUMENT_VALUE_CLOSE_PRICE,
                ],
            )
        ).instruments
        log.debug(f"market_values: {market_values}")


def get_fundamentals(client, asset_ids):
    with client as client:
        fundamentals = [
            fundamental for fundamental in
            client.instruments.get_asset_fundamentals(GetAssetFundamentalsRequest(asset_ids)).fundamentals
        ]
        log.debug(f"fundamentals: {fundamentals}")


def get_shares(client):
    with client as client:
        shares = [
            share for share in
            client.instruments.shares().instruments if filtered_data(share)
        ]
        log.debug(f"shares: {shares}")
        return shares


def get_portfolio(settings: Settings):
    token = settings.token.sandbox if settings.sandbox_mode else settings.token.read
    target = INVEST_GRPC_API_SANDBOX if settings.sandbox_mode else INVEST_GRPC_API
    log.debug(f"token: {token}, target: {target}")

    with Client(token=token, target=target) as client:
        log.info(client.users.get_accounts())
        log.info("accounts: {}".format(client.users.get_accounts()))
        log.info("info: {}".format(client.users.get_info()))

        portfolio = client.operations.get_portfolio(account_id=settings.account_id)
        log.info("portfolio: {}".format(portfolio))


if __name__ == "__main__":
    settings = utils.get_config(".private/settings.json")
    log.debug(f"settings: {settings}")
    invest_bot(settings)
    # get_portfolio(settings)
