# unit tests of ProductAdapter class

import unittest

from src.db.adapters.products_adapter import ProductAdapter


class TestProductAdapter(unittest.TestCase):
    def setUp(self):
        pass
    #     self.desc = ProductDescriptor(
    #         ID=None, 
    #         Name="",
    #         Description="",
    #         Quantity=0,
    #         Price=0.0,
    #         CreatedAt=None,
    #         LastUpdatedAt=None
    #     )

    # def test_create_product(self):
    #     p_obj = create_product("Product", self.desc)
    #     self.assertEqual(p_obj, Product(Descriptor=self.desc))

    # def test_create_product_sub(self):
    #     c_obj = create_product("Clothing", self.desc, Material="", Size="", Color="")
    #     self.assertEqual(c_obj, Clothing(Descriptor=self.desc, Material="", Size="", Color=""))

    # def test_create_product_nonexistent_type(self):
    #     with self.assertRaises(ValueError):
    #         fail = create_product("not a product", self.desc)


if __name__ == '__main__':
    unittest.main()