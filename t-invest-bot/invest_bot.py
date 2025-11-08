import pandas as pd
from tinkoff.invest import Client, GetAssetFundamentalsRequest
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX, INVEST_GRPC_API

import logger
import utils
from model import Settings

log = logger.get(__name__)


def invest_bot(settings: Settings):
    token = settings.token.sandbox if settings.sandbox_mode else settings.token.read
    target = INVEST_GRPC_API_SANDBOX if settings.sandbox_mode else INVEST_GRPC_API
    log.debug(f"token: {token}, target: {target}")

    with Client(token=token, target=target) as client:
        # log.info(client.users.get_accounts())
        # log.info("accounts: {}".format(client.users.get_accounts()))
        # log.info("info: {}".format(client.users.get_info()))

        shares = [
            (share.asset_uid, share.name, share.country_of_risk_name)
            for share in client.instruments.shares().instruments
            if (share.buy_available_flag and share.sell_available_flag)
        ]
        log.debug(f"shares: {shares[:5]}")

        # fundamentals = client.instruments.get_asset_fundamentals(GetAssetFundamentalsRequest(shares)).fundamentals
        # log.debug(f"fundamentals: {fundamentals}")
        # df_fundamentals = pd.DataFrame(fundamentals)
        # log.debug(f"df_fundamentals:\n{df_fundamentals[["ebitda_ttm", "net_debt_to_ebitda", "current_ratio_mrq"]]}")


if __name__ == "__main__":
    settings = utils.get_config(".private/settings.json")
    log.debug(f"settings: {settings}")
    invest_bot(settings)
