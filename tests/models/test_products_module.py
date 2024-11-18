# unit tests of products module

import unittest

from src.models import products as p


class TestProducts(unittest.TestCase):
    def setUp(self):
        # example instances from products module, 
        # created "traditionally" using their constructors
        self.product = p.Product(
            Name="product", 
            Description="description", 
            Quantity=1, 
            Price=1.00)
        self.clothing = p.Clothing(
            Name="clothing", 
            Description="description", 
            Quantity=1, 
            Price=1.00, 
            Material="cotton", 
            Size="L", 
            Color="blue")
        
        # dicts of the example instances' parameters
        self.product_dict = dict(
            Name=self.product.Name,
            Description=self.product.Description,
            Quantity=self.product.Quantity,
            Price=self.product.Price
        )
        self.clothing_dict = dict(
            Name=self.clothing.Name,
            Description=self.clothing.Description,
            Quantity=self.clothing.Quantity,
            Price=self.clothing.Price,
            Material=self.clothing.Material,
            Size=self.clothing.Size,
            Color=self.clothing.Color
        )
    
    # create()
    def test_create(self):
        obj = p.Product.create(
            "Product", 
            Name=self.product.Name,
            Description=self.product.Description,
            Quantity=self.product.Quantity,
            Price=self.product.Price)
        # is the object returned equal to self.product?
        self.assertEqual(obj, self.product)

    def test_create_subclass(self):
        obj = p.Product.create(
            "Clothing", 
            Name=self.clothing.Name,
            Description=self.clothing.Description,
            Quantity=self.clothing.Quantity,
            Price=self.clothing.Price,
            Material=self.clothing.Material,
            Size=self.clothing.Size,
            Color=self.clothing.Color)
        # is the same true for a subclass of Product?
        self.assertEqual(obj, self.clothing)

    def test_create_bad_type(self):
        with self.assertRaises(ValueError):
            p.Product.create("Not a valid product type", Name="", Description="", Quantity=0, Price=0.0)


    # create_from_dict()
    def test_create_from_dict(self):
        obj = p.Product.create_from_dict(Type="Product", self.product_dict)
        self.assertEqual(obj, self.product)

    def test_create_from_dict_subclass(self):
        obj = p.Product.create_from_dict(Type="Clothing", self.clothing_dict)
        self.assertEqual(obj, self.clothing)

    def test_create_from_dict_bad_dict(self):
        with self.assertRaises(ValueError):
            p.Product.create_from_dict({"Not a valid products class dict": "Not at all"})


    # _get_product_class_dynamically()
    def test_get_product_class_dynamically(self):
        c = p.product._get_product_class_dynamically("Product")
        self.assertEqual(c, p.Product)

    def test_get_product_class_dynamically_subclass(self):
        c = p.product._get_product_class_dynamically("Clothing")
        self.assertEqual(c, p.Clothing)


if __name__ == "__main__":
    unittest.main()
