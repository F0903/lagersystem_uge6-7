# main script to interact with a product management system
import os
import db.db_connection as db_con
from db.db_connection import DbConnection
from db.db_migrator import migrate_db
from db.adapters.product_adapter import ProductAdapter
from webserver.api import api


def main():
    is_docker = os.environ.get("DOCKER", False)
    if is_docker:
        db_con.DB_USER = os.environ["DB_USER"]
        db_con.DB_PASSWORD = os.environ["DB_PASSWORD"]
        db_con.DB_HOST = os.environ["DB_HOST"]
    else:
        print("Not running in Docker environment")

    db = DbConnection("lager")
    migrate_db(db, "migrations/")

    # Get the "api" for the products in the database
    products = ProductAdapter(db)

    # Just a test for fun
    for product in products.get_all_products(None):
        print(f"{product}")

    api.run()


if __name__ == "__main__":
    main()
