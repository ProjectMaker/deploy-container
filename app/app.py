from flask import Flask
from flask_cors import CORS
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

from config import get_config
from controller.webhook_controller import ns as ns_webhook

app = Flask(__name__)
CORS(app)
app.config.from_object(get_config())
app.wsgi_app = ProxyFix(app.wsgi_app)

app.url_map.strict_slashes = False


api = Api(app, version='2.0', title='Simulateur de devis')

api.add_namespace(ns_webhook, path='/api/webhook')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

