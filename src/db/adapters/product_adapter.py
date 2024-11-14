import dataclasses
from typing import Any, Generator, Iterable
from models.products import Product, ProductDescriptor
import mysql.connector as sql

from models.products import create_product_from_descriptor
from ..db_connection import DbConnection

PRODUCT_TABLE_NAME = "products"
PRODUCT_ATTRIBUTE_TABLE_NAME = "product_attributes"


class ProductAdapter:
    """
    An "adapter" that goes on top of the databse so provide a better API for
    operations regarding products.
    """

    def __init__(self, db: DbConnection) -> None:
        self._db = db

    def insert_product(self, product: Product):
        """
        Inserts the product into the products table.
        """

        # Transform dataclass to dictionary of field name -> value.
        attrs = dataclasses.asdict(product)

        # Get the descriptor to be used for product
        descriptor = attrs["Descriptor"]

        with self._db.get_cursor() as cur:
            # We first need to insert the product into the products table before the dynamic attributes.
            cur.execute(
                f"INSERT INTO {PRODUCT_TABLE_NAME} VALUES (DEFAULT, %s, %s, %s, %s, %s, DEFAULT, DEFAULT)",
                (
                    product.__class__.__name__,  # Use class name as the product type
                    descriptor["Name"],
                    descriptor["Description"],
                    descriptor["Quantity"],
                    descriptor["Price"],
                ),
            )

            # Then for each attribute, add an attribute row in the db.
            for name, value in attrs.items():
                # Skip the Descriptor
                if name == "Descriptor":
                    continue
                cur.execute(
                    f"INSERT INTO {PRODUCT_ATTRIBUTE_TABLE_NAME} VALUES (LAST_INSERT_ID(), %s, %s)",
                    (name, value),
                )

        self._db.commit()

    def update_product(self, product: Product):
        """
        Updates the product in the database.
        """

        # Transform dataclass to dictionary of field name -> value.
        attrs = dataclasses.asdict(product)
        descriptor = attrs["Descriptor"]
        product_id = descriptor["ID"]

        with self._db.get_cursor() as cur:
            # Update the manually set parts of the products table
            cur.execute(
                f"""
                UPDATE products
                SET
                    Name = %s,
                    Description = %s,
                    Quantity = %s,
                    Price = %s
                WHERE
                    ID = %s;
                """,
                (
                    descriptor["Name"],
                    descriptor["Description"],
                    descriptor["Quantity"],
                    descriptor["Price"],
                    product_id,
                ),
            )

            # Now set the other attribute values (if they exist for the product)
            for name, value in attrs.items():
                # Skip the Descriptor, which we have already done stuff with.
                if name == "Descriptor":
                    continue

                cur.execute(
                    f"""
                    UPDATE product_attributes
                    SET
                        AttributeValue = %s
                    WHERE
                        ProductID = %s AND
                        AttributeName = %s
                    """,
                    (value, product_id, name),
                )

        self._db.commit()

    def _get_attributes(
        self, cursor: sql.connection.MySQLCursor, product_id: int
    ) -> dict[str, Any]:
        """
        Get all attribute rows associated the the product id.
        """

        cursor.execute(
            f"SELECT * FROM {PRODUCT_ATTRIBUTE_TABLE_NAME} WHERE ProductID = %s",
            (product_id,),
        )
        attributes = cursor.fetchall()

        # Transform the attribute rows to dictionary of attribute_name -> attribute_value
        attributeDict = {}
        for attr in attributes:
            name = attr["AttributeName"]
            value = attr["AttributeValue"]
            attributeDict[name] = value

        return attributeDict

    def get_all_products(self, type: str | None) -> Iterable[Product]:
        """
        Get all the matching products from the database.

        New products are created with data from the products table,
        and additional attributes from product_attributes.
        """

        # Important to get the cursor as a dictionary cursor.
        # otherwise we can't get values by column name.
        with self._db.get_cursor(dictionary=True) as cur:

            # Determine whether we need to filter or not.
            if type is None:
                cur.execute(f"SELECT * FROM {PRODUCT_TABLE_NAME}")
            else:
                cur.execute(
                    f"SELECT * FROM {PRODUCT_TABLE_NAME} WHERE Type = %s", (type,)
                )

            # Get our products
            products = cur.fetchall()
            for row in products:
                descriptor = ProductDescriptor.create_from_dict(row)

                attributes = self._get_attributes(cur, descriptor.ID)
                product = create_product_from_descriptor(descriptor, **attributes)
                yield product
