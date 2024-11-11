# main script to interact with a product management system

from db.db import Db
from models.product import Clothing
from product_manager import ProductManager

if __name__ == "__main__":
    db = Db(user="root", password="root", host="localhost", database="lager")
