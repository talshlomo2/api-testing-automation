import pytest
from tests.base_test import BaseBotRequestTest
from tests import data
from api.enums import StatusCode, ErrorMessage
from api.bot_model import BotFields


class TestBotPatch(BaseBotRequestTest):
    """Test suite for PATCH requests on the bot API."""

    method = "PATCH"

    @pytest.mark.parametrize("intent", data.VALID_INTENTS)
    def test_patch_url_and_intents(self, create_and_delete_bot, intent):
        bot = {BotFields.URL: data.SECOND_VALID_URL, BotFields.INTENTS: [intent]}
        self.valid_request(bot, bot)

    def test_patch_bot_with_same_values(self, create_and_delete_bot):
        self.valid_request(data.VALID_BOT_WITH_ALL_FIELDS, data.VALID_BOT_WITH_ALL_FIELDS)

    def test_patch_bot_fields_to_empty(self, create_and_delete_bot):
        bot = {BotFields.URL: '', BotFields.INTENTS: []}
        self.valid_request(bot, bot)

    def test_patch_bot_url(self, create_and_delete_bot):
        bot_req = {BotFields.URL: data.SECOND_VALID_URL}
        bot_res = {BotFields.URL: data.SECOND_VALID_URL, BotFields.INTENTS: data.VALID_INTENTS}
        self.valid_request(bot_req, bot_res)

    @pytest.mark.parametrize("intent", data.VALID_INTENTS)
    def test_patch_bot_intents(self, create_and_delete_bot, intent):
        bot_req = {BotFields.INTENTS: [intent]}
        bot_res = {BotFields.URL: data.VALID_URL, BotFields.INTENTS: [intent]}
        self.valid_request(bot_req, bot_res)

    @pytest.mark.parametrize("invalid_url", data.INVALID_URLS)
    def test_patch_invalid_bot_url(self, create_and_delete_bot, invalid_url):
        bot = {BotFields.URL: invalid_url}
        self.invalid_request(StatusCode.BAD_REQUEST.value, ErrorMessage.INVALID_URL.value, bot)

    def test_patch_invalid_bot_intents(self, create_and_delete_bot):
        bot = {BotFields.INTENTS: [data.INVALID_INTENT]}
        self.invalid_request(StatusCode.BAD_REQUEST.value, ErrorMessage.INVALID_INTENTS.value, bot)

    def test_patch_unmodifiable_bot_field(self, create_and_delete_bot):
        bot = {BotFields.ID: data.ID}
        self.invalid_request(StatusCode.BAD_REQUEST.value, ErrorMessage.FIELDS_ERROR.value, bot)

    def test_patch_without_bot_name(self):
        self.request_without_sending_bot_name()
