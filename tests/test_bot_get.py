from tests import data
from tests.base_test import BaseBotRequestTest
from api.enums import StatusCode, ErrorMessage


class TestBotGet(BaseBotRequestTest):
    """Test suite for GET requests on the bot API."""

    method = "GET"

    def test_get_existing_bot(self, create_and_delete_bot):
        self.valid_request(bot_response=data.VALID_BOT_WITH_ALL_FIELDS)

    def test_get_non_existent_bot(self):
        self.invalid_request(StatusCode.NOT_FOUND.value, ErrorMessage.BOT_NOT_FOUND.value)

    def test_get_without_bot_name(self):
        self.request_without_sending_bot_name()
