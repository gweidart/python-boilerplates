import os

def get_config():
    config = {
        'API_KEY': os.getenv('API_KEY'),
        'DEBUG': os.getenv('DEBUG', 'False') == 'True'
    }
    return config
