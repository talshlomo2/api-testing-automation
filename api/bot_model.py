import json
import random


class BotFields:
    NAME = "name"
    ID = "id"
    URL = "url"
    INTENTS = "intents"


MODIFIABLE_FIELDS = [BotFields.URL, BotFields.INTENTS]


class Bot:
    """Bot class for representing a bot entity with ID, name, URL, and intents."""

    MIN_BOT_ID = 1
    MAX_BOT_ID = 1000

    def __init__(self, name, url, intents):
        self.id = random.randint(self.MIN_BOT_ID, self.MAX_BOT_ID)
        self.name = name
        self.url = url
        self.intents = intents

    def set_url(self, url):
        self.url = url

    def set_intents(self, intents):
        self.intents = intents

    def to_json(self):
        json_dict = {
            BotFields.ID: self.id,
            BotFields.NAME: self.name,
            BotFields.INTENTS: self.intents
        }
        if self.url:
            json_dict[BotFields.URL] = self.url

        return json.dumps(json_dict)
