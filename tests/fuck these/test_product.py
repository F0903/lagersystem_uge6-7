# unit tests of product class

import unittest
import datetime

from src.models.products.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product()

    def test_get_sql_values(self):
        vals = self.product.get_sql_values()

        self.assertEqual(vals[0], "")   # Name
        self.assertEqual(vals[1], "")   # Description
        self.assertEqual(vals[2], 0)    # Quantity
        self.assertEqual(vals[3], 0.0)  # Price
        self.assertEqual(type(vals[4]), datetime.datetime) # CreatedAt
    
    def test_get_sql_values_return_size(self):
        vals = self.product.get_sql_values()
        with self.assertRaises(IndexError):
            vals[5]


if __name__ == '__main__':
    unittest.main()