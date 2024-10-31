from enum import Enum
from api.db import Db


class StatusCode(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class ErrorMessage(Enum):
    BOT_NOT_FOUND = "Bot not found"
    BOT_EXISTS = "Bot with the same name already exists"
    INVALID_URL = "URL is not valid"
    FIELDS_ERROR = "You are allowed to modify only the intents and URL fields"
    INVALID_INTENTS = "The possible intents types are: {}".format(', '.join(Db.get_intents_list()))
    INVALID_INTENTS_FORMAT = "Intents should be in a list"
    REQUEST_WITHOUT_BOT_NAME = ("The requested URL was not found on the server. "
                                "If you entered the URL manually please check your spelling and try again")
