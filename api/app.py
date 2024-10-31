from flask import Flask, request
from flask_restful import Api, Resource
from api.bot_model import BotFields
from api.db import Db
from api.enums import StatusCode
from api import validations

app = Flask(__name__)
api = Api(app)


class BotsApi(Resource):
    """RESTful API resource for managing bot entities."""

    def post(self, name):
        validations.validate_bot_doesnt_exist(name)
        fields = self.validate_and_get_fields(self.post.__name__)
        Db.create_bot(name, fields[BotFields.URL], fields[BotFields.INTENTS])
        return Db.get_bot(name), StatusCode.CREATED.value

    def put(self, name):
        validations.validate_bot_exists(name)
        fields = self.validate_and_get_fields(self.put.__name__)
        Db.update_bot(name, fields[BotFields.URL], fields[BotFields.INTENTS])
        return Db.get_bot(name)

    def get(self, name):
        validations.validate_bot_exists(name)
        return Db.get_bot(name)

    def patch(self, name):
        validations.validate_bot_exists(name)
        fields = self.validate_and_get_fields(self.patch.__name__)
        Db.update_bot(name, fields[BotFields.URL], fields[BotFields.INTENTS])
        return Db.get_bot(name)

    def delete(self, name):
        validations.validate_bot_exists(name)
        Db.delete_bot(name)

    def validate_and_get_fields(self, method):
        """
        Validate and retrieve the 'url' and 'intents' fields from the request data.
        For 'patch' requests, sending None to the DB class ensures that the corresponding field is not updated,
        unless the user explicitly sends a value for that field, as 'patch' doesn't replace the entire object.
        """
        data = request.get_json()
        validations.validate_request_fields(data)
        url = self.validate_and_get_url(data, method)
        intents = self.validate_and_get_intents(data, method)
        return {BotFields.URL: url, BotFields.INTENTS: intents}

    def validate_and_get_url(self, data, method):
        url = None if method == 'patch' else ''
        if BotFields.URL in data:
            url = data[BotFields.URL]
            validations.validate_url(url)
        return url

    def validate_and_get_intents(self, data, method):
        intents = None if method == 'patch' else []
        if BotFields.INTENTS in data:
            intents = data[BotFields.INTENTS]
            validations.validate_intents(intents)
        return intents


api.add_resource(BotsApi, "/bot/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
