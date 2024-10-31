from api.bot_model import Bot


class Db:
    """A simple in-memory database class for managing bot data."""

    # db data
    __intents = ["play_sound", "tell_joke", "disconnect"]
    __bots = {}

    # intents related methods
    @classmethod
    def get_intents_list(cls):
        return cls.__intents

    # bots related methods
    @classmethod
    def get_bots(cls):
        return cls.__bots

    @classmethod
    def get_bot(cls, name):
        return cls.__bots[name].to_json()

    @classmethod
    def create_bot(cls, name, url, data_intents):
        cls.__bots[name] = Bot(name, url, data_intents)

    @classmethod
    def delete_bot(cls, name):
        del cls.__bots[name]

    @classmethod
    def update_bot(cls, name, url, data_intents):
        bot = cls.__bots[name]
        if url is not None:
            bot.set_url(url)
        if data_intents is not None:
            bot.set_intents(data_intents)
