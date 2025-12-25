import json

import logger
from model import Settings, TokenData, UrlData

log = logger.get(__name__)


def get_config(path: str) -> Settings | None:
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            token = TokenData(**data["token"])
            url = UrlData(**data["url"])
            settings = Settings(account_id=data["account_id"], token=token, sandbox_mode=data["sandbox_mode"], url=url)
            return settings
    except FileNotFoundError:
        log.error("File [{}] was not found".format(path))
    except Exception as e:
        log.error("Exception occurred while decoding the data from file [{}]".format(path))
        log.exception(e)
