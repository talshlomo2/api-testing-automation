import json
import requests
from tests import data
from api.enums import StatusCode, ErrorMessage
from api.bot_model import BotFields


class BaseBotRequestTest:
    """
    A base class for testing bot API requests, providing common methods for sending valid and invalid requests.
    method (str): The HTTP method to be used for requests. Subclasses should set this attribute to the desired method.
    """

    method = None

    def valid_request(self, bot_request=None, bot_response=None, expected_status=StatusCode.OK.value):
        response = requests.request(method=self.method, url=data.BASE_URL + data.BOT_NAME, json=bot_request)
        assert response.status_code == expected_status
        if bot_response is not None:
            self.check_bot_object_response(response, data.BOT_NAME, bot_response)

    def invalid_request(self, error_code, error_msg, bot=None):
        response = requests.request(method=self.method, url=data.BASE_URL + data.BOT_NAME, json=bot)
        assert response.status_code == error_code
        res_error_msg = response.json()
        excepted_error_msg = {"message": error_msg}
        assert res_error_msg == excepted_error_msg

    def request_without_sending_bot_name(self):
        response = requests.request(method=self.method, url=data.BASE_URL)
        assert response.status_code == StatusCode.NOT_FOUND.value
        assert ErrorMessage.REQUEST_WITHOUT_BOT_NAME.value in response.text

    # helper functions

    def check_bot_object_response(self, response, bot_name, bot_request):
        bot = json.loads(response.json())
        assert bot.get(BotFields.NAME) == bot_name
        assert type(bot.get(BotFields.ID)) is int

        bot_intents = bot_request.get(BotFields.INTENTS, [])
        assert bot.get(BotFields.INTENTS) == bot_intents

        bot_url = bot_request.get(BotFields.URL, '')
        if bot_url:
            assert bot.get(BotFields.URL) == bot_url
