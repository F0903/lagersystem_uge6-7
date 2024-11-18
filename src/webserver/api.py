from typing import Any
from flask import Flask, Request, jsonify, request, Response
from db.adapters.product_adapter import ProductAdapter
from db.db_connection import DbConnection
from models.products import Product, DbItemDescriptor
import db.db_error as db_err
from models.products.product import DatabaseProduct

api = Flask(__name__)


def _validate_product_fields(
    product_data: dict[str, Any]
) -> tuple[Response, int] | None:
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


def _validate_product_request(request: Request) -> tuple[Response, int] | dict:
    # Ensure the request body is JSON
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    product_data = request.get_json()[0]
    validate_error = _validate_product_fields(product_data)
    if validate_error:
        return validate_error

    return product_data


@api.route("/api/get/products")
def get_products() -> list[DatabaseProduct]:
    db = DbConnection()
    product_adapter = ProductAdapter(db)

    product_iter = product_adapter.get_all_products(None)
    # We need to return a list and not an iterator.
    return list(product_iter)


@api.route("/api/add/product", methods=["POST"])
def add_product():
    """
    Insert a product defined by the body of this request.
    """

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    assert_result = _validate_product_request(request)
    if isinstance(assert_result, tuple):  # Is result an error response tuple?
        return assert_result

    product = Product.create_from_dict(assert_result)

    try:
        product_adapter.insert_product(product)
    except db_err.DbError as err:
        return jsonify({"error": err.message}, 400)


# We don't use a parameter, as we get the ID directly off of the body
@api.route("/api/set/product/<int:id>", methods=["PUT"])
def set_product(id: int):
    """
    Replace a particular product by ID with the body of this request.
    """

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    assert_result = _validate_product_request(request)
    if isinstance(assert_result, tuple):  # Is result an error response tuple?
        return assert_result

    product = Product.create_from_dict(assert_result)

    try:
        product_adapter.update_product(product)
    except db_err.DbError as err:
        return jsonify({"error": err.message}, 400)
