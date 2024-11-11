# class managing a connection to a MySQL database

import mysql.connector as sql

from utils import singleton as singleton


@singleton
class Db:
    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        self.con = sql.MySQLConnection(user, password, host, database)

    def close(self):
        self.connection.close()

    def get():
        pass  # todo
