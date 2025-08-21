import json

class BotSettings:

    def __init__(self, name, link, token, feedback_email):
        self.name = name
        self.link = link
        self.token = token
        self.feedback_email = feedback_email

    def to_json(self):
        return json.dumps(self.__dict__, indent=2)
