import json
import os


class Config:

    def get(self, key):
        with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
            data = json.load(config_file)
        return data[key]
