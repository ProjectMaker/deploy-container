from flask import request
from flask_restplus import Namespace, Resource
from flask import current_app as app
from services.auth_service import verify_hook
from subprocess import call
ns = Namespace('webhook', description='USER Operations')

@ns.route('/')
class WebhookController(Resource):
    def post(self):
        if verify_hook(app.logger):
            call('cd /home/uniroulotte/ansible && ./deploy_api_uniroulotte.sh')

        return {}
