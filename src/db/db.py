
import mysql.connector as sql

from utils import singleton

@singleton
class Db:
    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        self.con = sql.MySQLConnection(user, password, host, database)
        self.unregister_singleton()

    def close():
        pass 
    
    def get():
        pass #todo