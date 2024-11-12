# main script to interact with a product management system

from db.db import Db
from product_manager import ProductManager

if __name__ == "__main__":
    #db = Db(user="root", password="root", host="localhost", database="lager")

    pm = ProductManager()
    my_shirt = pm.new_product("Clothing")
    my_shirt.Name = "my cool new shirt"
    my_shirt.Color = "red"
    print(my_shirt.get_sql_values())
    my_shirt.Description = "it is red"
    print(my_shirt.get_sql_values())
    print(vars(my_shirt))
