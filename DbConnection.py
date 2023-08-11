from sqlalchemy import create_engine

from Config import Config


class DbConnection(object):
    connections = {}

    def get_connection(self, config: str):
        db_config = self._validate_and_get_config(config)

        if self._get_connection_key(db_config) in self.connections.keys():
            return self.connections[self._get_connection_key(db_config)]

        engine = self._create_engine(db_config)

        connection = engine.connect()
        self.connections[self._get_connection_key(db_config)] = connection

        return connection

    @staticmethod
    def _validate_and_get_config(config: str) -> dict:
        assert config is not None
        db_config = Config().get(config)
        assert db_config is not None
        assert type(db_config) is dict
        assert 'username' in db_config.keys()
        assert 'password' in db_config.keys()
        assert 'server' in db_config.keys()
        assert 'port' in db_config.keys()
        assert 'dbname' in db_config.keys()
        return db_config

    @staticmethod
    def _get_connection_key(db_config: dict) -> str:
        return db_config['server'] + db_config['dbname']

    @staticmethod
    def _create_engine(db_config: dict):
        engine = create_engine(
            'mysql://' + str(db_config['username']) +
            ':' + str(db_config['password']) +
            '@' + str(db_config['server']) +
            ':' + str(db_config['port']) +
            '/' + str(db_config['dbname']) +
            '?charset=utf8mb4'
        )
        return engine
