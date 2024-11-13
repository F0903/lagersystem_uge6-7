# unit tests for product_manager module


import unittest

from product_manager import ProductManager

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.pm = ProductManager()

    def test_pm(self):
        print(self.pm)
        pass

# pm = ProductManager()
    # my_shirt = pm.new_product("Clothing")
    # my_shirt.Name = "my cool new shirt"
    # my_shirt.Color = "red"
    # print(my_shirt.get_sql_values())
    # my_shirt.Description = "it is red"
    # print(my_shirt.get_sql_values())
    # print(vars(my_shirt))


if __name__ == '__main__':
    unittest.main()