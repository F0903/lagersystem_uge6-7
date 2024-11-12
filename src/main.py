# main script to interact with a product management system

from db.db_connection import DbConnection
from db.db_migrator import migrate_db
from db.adapters.products_adapter import ProductAdapter
from models.product import Clothing, ProductDescriptor
import logging

LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)

# Create a console handler (prints logs to terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the console handler
console_handler_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_handler_formatter)

# Add the console handler to the logger
LOG.addHandler(console_handler)


def main():
    db = DbConnection(user="root", password="root", host="localhost", database="lager")
    migrate_db(db, "migrations/")

    test_product = Clothing(
        "Garbage bag",
        "XL",
        "Black",
        Descriptor=ProductDescriptor(
            ID=0,
            Name="Cut garbage bag",
            Description="Yes",
            Quantity=1,
            Price=1.05,
        ),
    )
    ProductAdapter(db).insert_product(test_product)


if __name__ == "__main__":
    main()
