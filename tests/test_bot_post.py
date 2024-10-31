import pytest
from tests.base_test import BaseBotRequestTest
from tests import data
from api.enums import StatusCode, ErrorMessage
from api.bot_model import BotFields


class TestBotPost(BaseBotRequestTest):
    """Test suite for POST requests on the bot API."""

    method = "POST"
    create_success_code = StatusCode.CREATED.value

    def test_create_bot_without_url_and_intents(self, delete_bot):
        self.valid_request({}, {}, self.create_success_code)

    def test_create_bot_with_url(self, delete_bot):
        bot = {BotFields.URL: data.VALID_URL}
        self.valid_request(bot, bot, self.create_success_code)

    @pytest.mark.parametrize("intent", data.VALID_INTENTS)
    def test_create_bot_with_one_intent(self, delete_bot, intent):
        bot = {BotFields.INTENTS: [intent]}
        self.valid_request(bot, bot, self.create_success_code)

    def test_create_bot_with_all_intents(self, delete_bot):
        bot = {BotFields.INTENTS: data.VALID_INTENTS}
        self.valid_request(bot, bot, self.create_success_code)

    def test_create_bot_with_url_and_intents(self, delete_bot):
        self.valid_request(data.VALID_BOT_WITH_ALL_FIELDS, data.VALID_BOT_WITH_ALL_FIELDS, self.create_success_code)

    @pytest.mark.parametrize("invalid_url", data.INVALID_URLS)
    def test_create_bot_with_invalid_url(self, invalid_url):
        bot = {BotFields.URL: invalid_url}
        self.invalid_request(StatusCode.BAD_REQUEST.value, ErrorMessage.INVALID_URL.value, bot)

    def test_create_bot_with_invalid_intents(self):
        bot = {BotFields.INTENTS: [data.INVALID_INTENT]}
        self.invalid_request(StatusCode.BAD_REQUEST.value, ErrorMessage.INVALID_INTENTS.value, bot)

    def test_create_bot_with_invalid_intent_format(self):
        bot = {BotFields.INTENTS: data.INVALID_INTENT_FORMAT}
        self.invalid_request(StatusCode.BAD_REQUEST.value, ErrorMessage.INVALID_INTENTS_FORMAT.value, bot)

    def test_create_existing_bot(self, create_and_delete_bot):
        self.invalid_request(StatusCode.CONFLICT.value, ErrorMessage.BOT_EXISTS.value)

    def test_create_without_bot_name(self):
        self.request_without_sending_bot_name()
