# unit tests of DbConnection class
# since this class is very simple this is mostly just a test of its singleton propety

import unittest

from src.db.db_connection import DbConnection


class TestDbConnection(unittest.TestCase):
    config = dict(
        user = "root",
        password = "Velkommen24",
        host = "localhost",
        database = "test_db"
    )

    def setUp(self):
        self.db_conn = DbConnection(**self.config)

    def tearDown(self):
        with self.db_conn.get_cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS `{self.config["database"]}`")


    # singleton-ness
    def test_singleton(self):
        """Testing that attempts to create new DbConnection instances return the already existing one"""
        new = DbConnection(user="New user", password="New password", host="New host", database="New database")
        self.assertEqual(new, self.db_conn)

    def test_singleton_unregister(self):
        """Testing that singleton can be reset and remade with new parameters"""
        new_db = "new_db"
        DbConnection.unregister_singleton()
        self.db_conn = DbConnection(
            user=self.config["user"], 
            password=self.config["password"], 
            host=self.config["host"], 
            database=new_db
            )
        with self.db_conn.get_cursor() as cur:
            cur.execute("SHOW DATABASES")
            result = [databases[0] for databases in cur.fetchall()]
            self.assertIn(new_db, result)
            cur.execute(f"DROP DATABASE `{new_db}`")
        

if __name__ == '__main__':
    unittest.main()