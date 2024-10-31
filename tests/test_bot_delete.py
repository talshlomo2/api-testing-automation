from tests.base_test import BaseBotRequestTest
from api.enums import StatusCode, ErrorMessage


class TestBotDelete(BaseBotRequestTest):
    """Test suite for DELETE requests on the bot API."""

    method = "DELETE"

    def test_delete_existing_bot(self, create_bot):
        self.valid_request()

    def test_delete_non_existent_bot(self):
        self.invalid_request(StatusCode.NOT_FOUND.value, ErrorMessage.BOT_NOT_FOUND.value)

    def test_delete_without_bot_name(self):
        self.request_without_sending_bot_name()
