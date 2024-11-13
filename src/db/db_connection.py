# class managing a connection to a MySQL database

import mysql.connector as sql

from utils.singleton import singleton


@singleton
class DbConnection:
    """
    A class representing a single Database connection.
    """

    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        self._con = sql.MySQLConnection(user=user, password=password, host=host)
        self._assert_database(database)

    def _assert_database(self, database_name: str):
        """
        Creates and sets active database if it does not exist on the server.
        """

        with self.get_cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`")
            cur.execute(f"USE `{database_name}`")

    def close(self):
        self._con.close()

    def get_cursor(
        self, *, buffered: bool = False, dictionary: bool = False
    ) -> sql.connection.MySQLCursor:
        """
        Returns MySQL cursor for internal use. (caller must dispose)
        """

        return self._con.cursor(buffered=buffered or dictionary, dictionary=dictionary)

    def commit(self):
        """
        Commit changes to the database.
        """
        self._con.commit()
