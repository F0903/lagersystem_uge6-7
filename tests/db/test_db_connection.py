# unit tests of DbConnection class, 
# also tests of singleton implementation

import unittest

from src.db.db_connection import DbConnection


class TestDbConnection(unittest.TestCase):
    config = dict(
        user = "my username",
        password = "my secret",
        host = "my machine",
        database = "my database"
    )

    def setUp(self):
        self.db_conn = DbConnection(**self.config)

    # _assert_database()

    # close()

    # get_cursor()

    # commit()

    # singleton-ness
    def test_singleton(self):
        """Testing that attempts to create new DbConnection instances return the already existing one"""
        new = DbConnection(user="Despite many changes", password="I remain eternal")
        self.assertEqual(new, self.db_conn)

    def test_singleton_unregister(self):
        """Testing that singleton can be reset and remade with new parameters"""
        DbConnection.unregister_singleton()
        self.db_conn = DbConnection(user="I was reset a moment ago")
        self.assertNotEqual(self.db_conn.user, self.config["user"])
        


if __name__ == '__main__':
    unittest.main()