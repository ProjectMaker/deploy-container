import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class BaseConfig(object):
    ORIGINS = ['*']
    PORT = 5001

class Development(BaseConfig):
    DEBUG = True

config = {
    'development': 'config.Development'
}


def get_config():
    return config[os.getenv('FLASK_ENV')]
