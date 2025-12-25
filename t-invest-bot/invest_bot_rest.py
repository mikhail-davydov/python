import json

import requests

import logger
import utils
from model import Settings

log = logger.get(__name__)


def invest_bot_rest(settings: Settings):
    token = settings.token.sandbox if settings.sandbox_mode else settings.token.read
    target = settings.url.sandbox if settings.sandbox_mode else settings.url.live
    log.debug(f"token: {token}, target: {target}")

    shares = get_shares(target, token)

    share_ids = [share["assetUid"] for share in shares]
    get_fundamentals(share_ids, target, token)

    instrument_ids = [share["uid"] for share in shares]
    get_market_values(instrument_ids, target, token)


def get_market_values(instrument_ids, target, token):
    url = target + "/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetMarketValues"
    log.debug(f"url: {url}")

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        "instrumentId": instrument_ids,
        # "values": [
        #     "INSTRUMENT_VALUE_UNSPECIFIED"
        # ]
    }

    response = requests.post(url, json=payload, headers=headers).json()
    market_values = list(response["instruments"])
    log.debug(f"market_values: {json.dumps(market_values, indent=4, ensure_ascii=False)}")

    return market_values


def get_fundamentals(share_ids, target, token):
    url = target + "/rest/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetAssetFundamentals"
    log.debug(f"url: {url}")

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        "assets": share_ids,
    }

    response = requests.post(url, json=payload, headers=headers).json()
    fundamentals = list(response["fundamentals"])
    log.debug(f"fundamentals: {json.dumps(fundamentals, indent=4, ensure_ascii=False)}")

    return fundamentals


def get_shares(target, token):
    url = target + "/rest/tinkoff.public.invest.api.contract.v1.InstrumentsService/Shares"
    log.debug(f"url: {url}")

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {}

    response = requests.post(url, json=payload, headers=headers).json()
    shares = list(filter(filter_shares, response["instruments"]))
    log.debug(f"shares: {json.dumps(shares, indent=4, ensure_ascii=False)}")

    return shares


def filter_shares(item):
    return (
            item["buyAvailableFlag"]
            and item["sellAvailableFlag"]
            and item["name"] == "ВК"
    )


def get_portfolio(settings: Settings):
    token = settings.token.sandbox if settings.sandbox_mode else settings.token.read
    target = settings.url.sandbox if settings.sandbox_mode else settings.url.live
    log.debug(f"token: {token}, target: {target}")

    url = target + "/rest/tinkoff.public.invest.api.contract.v1.OperationsService/GetPortfolio"
    log.debug(f"url: {url}")

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        "accountId": settings.account_id
    }

    portfolio = requests.post(url, json=payload, headers=headers).json()
    log.debug(f"portfolio: {json.dumps(portfolio, indent=4, ensure_ascii=False)}")


if __name__ == "__main__":
    settings = utils.get_config(".private/settings.json")
    log.debug(f"settings: {settings}")
    invest_bot_rest(settings)
    # get_portfolio(settings)
