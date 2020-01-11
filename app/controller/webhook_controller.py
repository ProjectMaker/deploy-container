from flask import request
from flask_restplus import Namespace, Resource

from services.auth_service import verify_hook
ns = Namespace('webhook', description='USER Operations')

@ns.route('/')
class WebhookController(Resource):
    def post(self):
        print(verify_hook())
        # print(request.get_json())

        return {}
