# main script to interact with a product management system

from db.db_connection import DbConnection
from db.db_migrator import migrate_db
from db.adapters.product_adapter import ProductAdapter
from models.products import Clothing, ProductDescriptor
from webserver.api import api


def main():
    db = DbConnection(database="lager")
    migrate_db(db, "migrations/")

    # Get the "api" for the products in the database
    products = ProductAdapter(db)

    # Just a test for fun
    for product in products.get_all_products(None):
        print(f"{product}")

    api.run()


if __name__ == "__main__":
    main()
