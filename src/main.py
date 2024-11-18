# main script to interact with a product management system
import os
from .db.db_connection import DbConnection
from .db.migrate import migrate_db
from .db.adapters.product_adapter import ProductAdapter
from .webserver.api import api


def main():
    is_docker = os.environ.get("DOCKER", False)

    if is_docker:
        user = os.environ["DB_USER"]
        password = os.environ["DB_PASSWORD"]
        host = os.environ["DB_HOST"]
    else:
        print("Not running in Docker environment")
        user = "root"
        password = "root"
        host = "localhost"

    db = DbConnection(user, password, host, "lager")
    migrate_db(db, "migrations/")

    # Get the "api" for the products in the database
    products = ProductAdapter(db)

    # Just a test for fun
    for product in products.get_all_products(None):
        print(f"{product}")

    api.run()


if __name__ == "__main__":
    main()
