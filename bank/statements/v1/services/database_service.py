import psycopg2
from psycopg2.extras import RealDictCursor

from django.conf import settings


class Database(object):

    def __init__(self, dbname='default'):
        self.dbname = dbname
        self.connection = self.__connection()

    def __connection(self):
        credentials = settings.DATABASES[self.dbname]
        conn_string = '''host={host} dbname={dbname} user={user} password={password} port={port}'''.format(
            host=credentials['HOST'],
            dbname=credentials['NAME'],
            user=credentials['USER'],
            password=credentials['PASSWORD'],
            port=credentials['PORT'])
        conn = psycopg2.connect(conn_string)
        return conn

    def execute_query(self, query):
        cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        self.connection.commit()
        return cursor

    def close_connection(self):
        self.connection.close()
