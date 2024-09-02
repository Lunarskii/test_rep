import psycopg2
import logging


logger = logging.getLogger('Database')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            try:
                instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
                cls._instances[cls] = instance
            except Exception as e:
                if cls in cls._instances:
                    del cls._instances[cls]
                raise e
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    def __init__(self, uri: str):
        logger.info(f'Connecting to the database. \'{uri}\'')
        self._connection = psycopg2.connect(uri)
        logger.info('The connection has been successfully established.')

    def __del__(self):
        logger.info('Disconnecting from the database.')
        self._connection.close()
        logger.info('The connection has been disconnected.')

    def cursor(self):
        return self._connection.cursor()
