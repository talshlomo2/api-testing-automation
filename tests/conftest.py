import pytest
import requests
from tests import data


@pytest.fixture
def create_bot():
    """Fixture to create a valid bot with all the fields before the test."""
    requests.post(data.BASE_URL + data.BOT_NAME, json=data.VALID_BOT_WITH_ALL_FIELDS)


@pytest.fixture
def delete_bot():
    """Fixture to delete a bot after test."""
    yield
    requests.delete(data.BASE_URL + data.BOT_NAME)


@pytest.fixture
def create_and_delete_bot(create_bot, delete_bot):
    """Fixture combining the create_bot and delete_bot fixtures to create and delete a bot for testing."""
    pass
