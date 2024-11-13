from typing import Any
from flask import Flask, jsonify, request

from db.adapters.products_adapter import ProductAdapter
from db.db_connection import DbConnection
from models.products.product import Product

api = Flask(__name__)
db = DbConnection("lager")


@api.route("/api/get/products")
def get_products() -> list[Product]:
    product_adapter = ProductAdapter(db)
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


@api.route("/apt/set/product/<int:productID>", methods=["PUT"])
def set_product(productID: int):
    # Ensure the request body is JSON
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    product_data = request.get_json()
    _validate_product_fields(product_data)

    product_descriptor = product_data["Descriptor"]
    for name, value in product_data:
        # We already have the
        if name == "Descriptor":
            continue
