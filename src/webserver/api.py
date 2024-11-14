from typing import Any
from flask import Flask, jsonify, request

from db.adapters.product_adapter import ProductAdapter
from db.db_connection import DbConnection
from models.products import Product, ProductDescriptor, create_product_from_dict

api = Flask(__name__)
db = DbConnection("lager")
product_adapter = ProductAdapter(db)


@api.route("/api/get/products")
def get_products() -> list[Product]:
    product_iter = product_adapter.get_all_products(None)
    # We need to return a list and not an iterator.
    return list(product_iter)


def _validate_product_fields(product_data: dict[str, Any]):
    """
    Validate that the request data has the minimum required fields.
    """

    required_fields = ["Descriptor"]
    if not all(field in product_data for field in required_fields):
        return (
            jsonify(
                {
                    "error": f"Missing required fields. Required fields are: {required_fields}"
                }
            ),
            400,
        )


# We don't use a parameter, as we get the ID directly off of the body
@api.route("/api/set/product", methods=["PUT"])
def set_product():
    """
    Replace a particular product by ID with the body of this request.
    """

    # Ensure the request body is JSON
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    product_data = request.get_json()[0]
    validate_error = _validate_product_fields(product_data)
    if validate_error:
        return validate_error

    product = create_product_from_dict(product_data)
    product_adapter.update_product(product)
