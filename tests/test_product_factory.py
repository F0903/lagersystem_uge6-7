# unit tests of ProductFactory class (with a hint of integration tests for products module)

import unittest
import datetime

# from src.models.products.factories.product_factory import ProductFactory
from src.models.products.factories.product_factory import create_product
from src.models.products.product import Product, DbItemDescriptor
from src.models.products.clothing import Clothing


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.desc = DbItemDescriptor(
            ID=None,
            Name="",
            Description="",
            Quantity=0,
            Price=0.0,
            CreatedAt=None,
            LastUpdatedAt=None,
        )

    def test_create_product(self):
        p_obj = create_product("Product", self.desc)
        self.assertEqual(p_obj, Product(Descriptor=self.desc))

    def test_create_product_sub(self):
        c_obj = create_product("Clothing", self.desc, Material="", Size="", Color="")
        self.assertEqual(
            c_obj, Clothing(Descriptor=self.desc, Material="", Size="", Color="")
        )

    # def test_get_sql_values(self):
    #     vals = self.product.get_sql_values()

    #     self.assertEqual(vals[0], "")   # Name
    #     self.assertEqual(vals[1], "")   # Description
    #     self.assertEqual(vals[2], 0)    # Quantity
    #     self.assertEqual(vals[3], 0.0)  # Price
    #     self.assertEqual(type(vals[4]), datetime.datetime) # CreatedAt

    # def test_get_sql_values_return_size(self):
    #     vals = self.product.get_sql_values()
    #     with self.assertRaises(IndexError):
    #         vals[5]


if __name__ == "__main__":
    unittest.main()
