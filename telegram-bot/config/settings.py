import json

from logger import get_logger

logger = get_logger(__name__)


class BotSettings:

    def __init__(self, name, link, token, feedback_email):
        self.name = name
        self.link = link
        self.token = token
        self.feedback_email = feedback_email

    def to_json(self):
        return json.dumps(self.__dict__, indent=2)


def read_config(file_path):
    logger.info("Path to settings file: %s", file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
        return BotSettings(**data)
