# main script to interact with a product management system

from db.db import Db
from models.product import Clothing
from product_manager import ProductManager

if __name__ == "__main__":
    # db = Db()

    pm = ProductManager()
    o = pm.new_product("Clothing")
    
    print(o.get_sql_values())
    
