from datetime import datetime, timedelta, timezone
import logging
import os
from typing import Any
from flask import Flask, Request, jsonify, make_response, request, Response
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)
from ..utils.read_file import read_file_as_str
from ..models.products import Product
from ..db.adapters.product_adapter import ProductAdapter
from ..db.adapters.user_adapter import UserAdapter
from ..db.db_connection import DbConnection
from ..db.db_product import DatabaseProduct
from ..db import error as db_err


LOG = logging.getLogger(__name__)

api = Flask(__name__)
api.json.sort_keys = False

# CORS (i hate this)
CORS(api)

# Setup the Flask-JWT-Extended extension
api.config["JWT_SECRET_KEY"] = read_file_as_str(os.environ["JWT_SECRET_FILE"])
api.config["JWT_ACCESS_COOKIE_NAME"] = "token"
api.config["JWT_COOKIE_SECURE"] = False  # Set this to true if ever running HTTPS
api.config["JWT_TOKEN_LOCATION"] = "cookies"
api.config["JWT_ACCESS_COOKIE_PATH"] = "/"
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=6)
jwt = JWTManager(api)


def _validate_product_request_fields(
    product_data: dict[str, Any]
) -> tuple[Response, int] | None:
    """
    Validate that the request data has the minimum required fields.
    """

    required_fields = ["Type", "Product"]
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

    json = request.get_json()
    product_data = json
    validate_error = _validate_product_request_fields(product_data)
    if validate_error:
        return validate_error

    return product_data


# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@api.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


@api.route("/api/login", methods=["POST"])
def login():
    json = request.get_json()
    username = json["Username"]
    password = json["Password"]

    LOG.info(f"Attempting login with username '{username}'")
    LOG.debug(f"and password '{password}'")

    db = DbConnection()
    user_adapter = UserAdapter(db)

    unauth_response = jsonify({"error": "Bad username or password."}), 401

    try:
        user = user_adapter.get_user_by_username(username)
        if not user:
            LOG.info(f"User '{username}' did not exist in database.")
            return unauth_response
    except db_err.DbError as err:
        LOG.info("Generic DB error when attempting to login.")
        return jsonify({"error": err.message}), 500

    if not user.is_password_match(password):
        LOG.info(f"Wrong password used with username '{username}'")
        return unauth_response

    claims = {}

    if user.IsAdmin:
        claims["role"] = "admin"

    token = create_access_token(
        identity=username,
        additional_claims=claims,
    )

    response = make_response(jsonify({"message": "Login successful"}))
    set_access_cookies(response, token)

    return response


@api.route("/api/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@api.route("/api/products", methods=["GET"])
@jwt_required()
def get_products() -> list[DatabaseProduct]:
    LOG.debug(f"Received get products request: {request}")

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    type_filter = request.args.get("type_filter", None)

    try:
        product_iter = product_adapter.get_all_products(type_filter)
    except db_err.DbError as err:
        return jsonify({"error": err.message}), 400
    # We need to return a list and not an iterator.
    return list(product_iter)


@api.route("/api/product/<int:id>", methods=["GET"])
@jwt_required()
def get_product(id: int):
    LOG.debug(f"Received get product request: {request}")

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    try:
        product = product_adapter.get_product(id)
    except db_err.DbError as err:
        return jsonify({"error": err.message}), 400

    return [product]


@api.route("/api/product", methods=["POST"])
@jwt_required()
def add_product():
    """
    Insert a product defined by the body of this request.
    """

    LOG.debug(f"Received add product request: {request}")

    assert_result = _validate_product_request(request)
    if isinstance(assert_result, tuple):  # Is result an error response tuple?
        return assert_result

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    type_str = assert_result["Type"]
    product_dict = assert_result["Product"]
    product = Product.create_from_dict(type_str, product_dict)

    try:
        product_adapter.insert_product(product)
        db.commit()
    except db_err.DbError as err:
        return jsonify({"error": err.message}), 400

    return "Success"


@api.route("/api/product/<int:id>", methods=["PUT"])
@jwt_required()
def set_product(id: int):
    """
    Replace a particular product by ID with the body of this request.
    """

    LOG.debug(f"Received set product request: {request}")

    assert_result = _validate_product_request(request)
    if isinstance(assert_result, tuple):  # Is result an error response tuple?
        return assert_result

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    type_str = assert_result["Type"]
    product_dict = assert_result["Product"]
    product = Product.create_from_dict(type_str, product_dict)

    try:
        product_adapter.update_product(id, product)
        db.commit()
    except db_err.DbError as err:
        return jsonify({"error": err.message}), 400

    return "Success"


@api.route("/api/product/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id: int):
    LOG.debug(f"Received delete product request: {request}")

    db = DbConnection()
    product_adapter = ProductAdapter(db)

    try:
        product_adapter.delete_product(id)
        db.commit()
    except db_err.DbError as err:
        return jsonify({"error": err.message}), 400

    return "Success"
