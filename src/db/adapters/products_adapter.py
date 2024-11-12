import dataclasses
from db.db_connection import DbConnection
from models.product import Product

PRODUCT_TABLE_NAME = "products"
PRODUCT_ATTRIBUTE_TABLE_NAME = "product_attributes"


class ProductAdapter:
    def __init__(self, db: DbConnection) -> None:
        self._db = db

    def insert_product(self, product: Product):
        attrs = dataclasses.asdict(product)
        descriptor = attrs["Descriptor"]

        with self._db.get_cursor() as cur:
            # We first need to insert the product into the products table
            cur.execute(
                f"INSERT INTO {PRODUCT_TABLE_NAME} VALUES (DEFAULT, %s, %s, %s, %s, %s, DEFAULT)",
                (
                    product.__class__.__name__,  # Use class name as the product type
                    descriptor["Name"],
                    descriptor["Description"],
                    descriptor["Quantity"],
                    descriptor["Price"],
                ),
            )

            # Then we can add an attribute instance
            for i, tupl in enumerate(attrs.items()):
                # Skip the first one (the Descriptor)
                if i == 0:
                    continue
                name, value = tupl
                cur.execute(
                    f"INSERT INTO {PRODUCT_ATTRIBUTE_TABLE_NAME} VALUES (LAST_INSERT_ID(), %s, %s)",
                    (name, value),
                )

        self._db.commit()

    def get_all_product(self) -> list[Product]:
        with self._db.get_cursor() as cur:
            cur.execute(f"SELECT * FROM {PRODUCT_TABLE_NAME}")
            products = cur.fetchall()
