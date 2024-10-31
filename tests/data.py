from api.db import Db
from api.bot_model import BotFields

# api url
BASE_URL = "http://127.0.0.1:5000/bot/"

# valid inputs
BOT_NAME = "tal-bot"
VALID_URL = "http://example.com"
SECOND_VALID_URL = "https://testing.com"
VALID_INTENTS = Db.get_intents_list()
VALID_BOT_WITH_ALL_FIELDS = {BotFields.URL: VALID_URL, BotFields.INTENTS: VALID_INTENTS}

# invalid inputs
INVALID_URLS = ["htt://example.com", "example.com", "http://"]
INVALID_INTENT = "automation"
INVALID_INTENT_FORMAT = "format"
ID = 100
