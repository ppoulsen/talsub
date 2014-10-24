#
# connection.py
# A module for wrapping MongoDB connection details.
#

from mongoengine.connection import connect, disconnect, get_connection
from shared.config import get_config


class DBConnection(object):
    """A class that encapsulates the MongoDB connection."""

    def __init__(self):
        kwargs = {
            'db': get_config('data', 'dbname'),
            'host': get_config('data', 'host'),
            'port': get_config('data', 'port', is_int=True)
        }

        user = get_config('data', 'user')
        if user:
            kwargs['user'] = user

        password = get_config('data', 'password')
        if password:
            kwargs['password'] = password

        disconnect()
        connect(**kwargs)
        self.conn = get_connection()

    def __enter__(self):
        return self

    def __exit__(self, ext, exv, trb):
        disconnect()