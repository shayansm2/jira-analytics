import yaml

from lib.SingletonMeta import SingletonMeta


class Config(object, metaclass=SingletonMeta):
    config_path = 'configs.yml'
    config = None

    def __init__(self):
        file = open(self.config_path, 'r')
        self.config = yaml.load(file, yaml.FullLoader)

    def get(self, key: str):
        keys = key.split('.')
        config = self.config

        for key in keys:
            config = config.get(key)
            if config is None:
                return None

        return config
