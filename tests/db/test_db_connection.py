# unit tests of DbConnection class, 
# also tests of singleton implementation

import unittest

from src.db.db_connection import DbConnection


class TestDbConnection(unittest.TestCase):
    def setUp(self):
        self.db_conn = DbConnection()

    # _assert_database()

    # close()

    # get_cursor()

    # commit()

    # singleton-ness
    def test_singleton(self):
        """Tests that attempts to create new DbConnection instances return the already existing one"""
        new = DbConnection()
        self.assertEqual(new, self.db_conn)

    # def test_singleton_unregister(self):
    #     """Tests that singleton can be overwritten with new parameters?"""
    #     new = DbConnection(user="new")
    #     self.assertNotEqual(new, self.db_conn)


if __name__ == '__main__':
    unittest.main()