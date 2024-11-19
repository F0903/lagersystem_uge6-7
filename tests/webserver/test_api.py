# unit tests of webserver/api.py, the backend letting clients interact with the database

import unittest

from src.webserver.api import api
api.testing = True

from src.db.db_connection import DbConnection
from src.db.db_item_descriptor import DbItemDescriptor
from src.db.migrate import migrate_db
from src.models import products as p
from tests.config import db_config

test_HOST = "localhost"
test_PORT = 5100
test_URL = f"http://{test_HOST}:{test_PORT}"

class Testapi(unittest.TestCase):
    config_product = dict(
        Name="testProduct", 
        Description="Test description", 
        Quantity=1, 
        Price=1.00
    )

    def setUp(self):
        # start each test from a fresh database
        self.db_conn = DbConnection(**db_config)
        self.db_conn._assert_database(db_config["database"])
        migrate_db(self.db_conn, "migrations/")

    def tearDown(self):
        # remove testing database after each test
        with self.db_conn.get_cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS `{db_config["database"]}`")


    # get_product()
    # TODO: get nonexistant product
    def test_get_product(self):
        """Add, then get product"""
        with api.test_client() as client:
            data = {"Type": "Product", "Product": self.config_product}
            client.post('/api/product', json=data)
            
            res = client.get('/api/product/1')
            product = p.Product.create_from_dict("Product", eval(res.data)[0]["Product"])
            # dbid wont be used for assert but this is just to check if the returned dict is valid
            dbid = DbItemDescriptor.create_from_dict(eval(res.data)[0]["Descriptor"])

            # eval() doesn't convert the float in the response to a float type
            # so this typecasting is just to help out
            # ideally there should be a function that unwraps backend responses properly
            product.Price = float(product.Price)
            self.assertEqual(product, p.Product(**self.config_product))


    # get_products()

    # add_product()
    # TODO: add_product() duplicate entry
    def test_add_product(self):
        with api.test_client() as client:
            data = {"Type": "Product", "Product": self.config_product}
            res = client.post('/api/product', json=data)
            self.assertEqual(res.get_data(as_text=True), "Success")

    # set_product()

    # delete_product()

    # _validate_product_request()

    # _validate_product_request_fields()


if __name__ == "__main__":
    unittest.main()
