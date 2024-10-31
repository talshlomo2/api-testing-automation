import validators
from flask_restful import abort
from api.enums import StatusCode, ErrorMessage
from api.bot_model import MODIFIABLE_FIELDS
from api.db import Db

"""
Validation functions for the Bot API, including checks for request fields, URL, intents, and bot existence.
abort(status_code, message) is called if validation fails.
"""


def validate_request_fields(data):
    for field in data.keys():
        if field not in MODIFIABLE_FIELDS:
            abort(StatusCode.BAD_REQUEST.value, message=ErrorMessage.FIELDS_ERROR.value)


def validate_url(url):
    if not validators.url(url) and url:
        abort(StatusCode.BAD_REQUEST.value, message=ErrorMessage.INVALID_URL.value)


def validate_intents(intents):
    if type(intents) is not list:
        abort(StatusCode.BAD_REQUEST.value, message=ErrorMessage.INVALID_INTENTS_FORMAT.value)

    for intent in intents:
        if intent not in Db.get_intents_list():
            abort(StatusCode.BAD_REQUEST.value, message=ErrorMessage.INVALID_INTENTS.value)


def validate_bot_exists(name):
    if name not in Db.get_bots():
        abort(StatusCode.NOT_FOUND.value, message=ErrorMessage.BOT_NOT_FOUND.value)


def validate_bot_doesnt_exist(name):
    if name in Db.get_bots():
        abort(StatusCode.CONFLICT.value, message=ErrorMessage.BOT_EXISTS.value)
