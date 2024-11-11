# class managing a connection to a MySQL database

from typing import Any
import mysql.connector as sql

from utils.singleton import singleton


@singleton
class Db:
    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        self.con = sql.MySQLConnection(user, password, host, database)

    def close(self):
        self.con.close()

    def get_one(self, table: str) -> tuple[Any] | None:
        cursor = self.con.cursor()

        # Select all from table
        cursor.execute(f"SELECT * FROM {table}")

        result = cursor.fetchone()
        self.con.commit()

    def add_one(self, table: str, row: tuple[Any]):
        cursor = self.con.cursor()

        row_str = row.__str__()
        cursor.execute(f"INSERT INTO {table} ({row_str})")
        self.con.commit()
