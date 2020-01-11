from flask import request
from flask_restplus import Namespace, Resource

ns = Namespace('webhook', description='USER Operations')

@ns.route('/')
class WebhookController(Resource):
    def post(self):
        print(request.get_json())

        return {}
