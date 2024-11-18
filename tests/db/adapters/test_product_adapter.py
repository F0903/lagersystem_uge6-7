# unit tests of ProductAdapter class

import unittest

from src.db.adapters.product_adapter import ProductAdapter
from src.db.db_connection import DbConnection
from src.db.db_migrator import migrate_db
from src.db import db_error
from src.models import products as p


class TestProductAdapter(unittest.TestCase):
    config_db_conn = dict(
        user = "root",
        password = "Velkommen24",
        host = "localhost",
        database = "test_db"
    )
    config_product = dict(
        Name="testProduct", 
        Description="Test description", 
        Quantity=1, 
        Price=1.00
    )
    config_clothing = dict(
        Name="testClothing", 
        Description="Test description", 
        Quantity=5, 
        Price=6.50, 
        Material="Cotton", 
        Size="L", 
        Color="Blue"
    )

    def setUp(self):
        # start each test from a fresh database
        self.db_conn = DbConnection(**self.config_db_conn)
        self.db_conn._assert_database(self.config_db_conn["database"])
        migrate_db(self.db_conn, "migrations/")
        self.pa = ProductAdapter(self.db_conn)


    def tearDown(self):
        # remove testing database after each test
        with self.db_conn.get_cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS `{self.config_db_conn["database"]}`")


    # get_product() (coming soon TODO)
    # testing side effects of insert, delete, update


    # insert_product() TODO get_product()
    def test_insert_product(self):
        self.pa.insert_product(p.Product(**self.config_product))

    def test_insert_product_subclass(self):
        self.pa.insert_product(p.Clothing(**self.config_clothing))

    def test_insert_product_several(self):
        self.pa.insert_product(p.Product(**self.config_product))
        self.pa.insert_product(p.Clothing(**self.config_clothing))

    def test_insert_product_repeats(self):
        self.pa.insert_product(p.Product(**self.config_product))
        with self.assertRaises(db_error.DuplicateEntryError):
            self.pa.insert_product(p.Product(**self.config_product))


    # update_product() TODO get_product()
    def test_update_product(self):
        self.pa.insert_product(p.Product(**self.config_product))

        new_product = p.Product(**self.config_product)
        new_product.Price = 10000.5
        self.pa.update_product(1, new_product)

    def test_update_product_new_class(self):
        """Updating product with an instance of product subclass"""
        self.pa.insert_product(p.Product(**self.config_product))

        actually_clothing = p.Clothing(**self.config_clothing)
        self.pa.update_product(1, actually_clothing)


    # delete_product() (coming soon TODO)

    # _get_extra_attributes()

    # get_all_products()
    def test_get_all_products(self):
        self.pa.insert_product(p.Product(**self.config_product))

        items = self.pa.get_all_products(type=None)
        count = 0
        for _ in items:
            count += 1
        self.assertEqual(count, 1)

    def test_get_all_products_several(self):
        self.pa.insert_product(p.Product(**self.config_product))
        self.pa.insert_product(p.Clothing(**self.config_clothing))

        items = self.pa.get_all_products(type=None)
        count = 0
        for _ in items:
            count += 1
        self.assertEqual(count, 2)

    def test_get_all_products_one_type(self):
        self.pa.insert_product(p.Product(**self.config_product))
        self.pa.insert_product(p.Clothing(**self.config_clothing))

        items = self.pa.get_all_products(type="Clothing")
        count = 0
        for _ in items:
            count += 1
        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()