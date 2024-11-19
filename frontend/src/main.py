import click
import requests
from .utils import _args_to_dict

HOST = "localhost"
PORT = 5000
URL_BASE = f"http://{HOST}:{PORT}"


def _print_bad_response(response):
    click.echo(
        f"Error. Response was not 200 (OK). \nResponse was: {response.status_code}\n{response.content}",
        err=True,
    )


def _get_product_json(id: str) -> dict | None:
    """
    Get product from the server with ID, and turn response into JSON dict.
    """

    response = requests.get(f"{URL_BASE}/api/product/{id}")
    if response.status_code != 200:
        _print_bad_response(response)
        return None
    return response.json()


@click.group("api")
def api():
    pass


@api.command()
@click.option(
    "--filter",
    help="Filter for product type.",
)
def get_products(filter: str | None):
    """
    Gets all products.
    """

    filter_query = None if filter is None else {"type_filter": filter}
    response = requests.get(f"{URL_BASE}/api/products", params=filter_query)
    body = response.json()

    # TODO: pretty print the JSON response?
    click.echo(body)


@api.command()
@click.option(
    "--id",
    required=True,
    help="The ID of the product to retrieve.",
)
def get_product(id: str):
    """
    Get a single product matching the ID.
    """

    product = _get_product_json(id)
    if not product:
        return
    click.echo(product)


@api.command()
@click.option(
    "--id",
    required=True,
    help="The ID of the product to set.",
)
@click.argument(
    "product_fields",
    nargs=-1,
    callback=_args_to_dict,
)
def set_product(id: str, product_fields: dict[str, str]):
    """
    Update the fields of the product with the specified ID.
    Field arguments are specified as described, with a space between: 'name=value'
    """

    # First we get the product as it is now.
    product = _get_product_json(id)
    if not product:
        return

    db_item = product[0]
    descriptor = db_item["Descriptor"]

    product_type = descriptor["Type"]
    product = db_item["Product"]

    # Go through the common keys in each
    common_keys = [k for k in product_fields.keys() if k in product]
    if not common_keys:
        click.echo("No matching fields in product... Did you misspell the fields?")

    for key in common_keys:
        value = product_fields[key]
        product[key] = value
        click.echo(f"Set field '{key}' = '{value}'")

    # Now send the modified product
    body = {"Type": product_type, "Product": product}
    response = requests.put(f"{URL_BASE}/api/product/{id}", json=body)
    if response.status_code != 200:
        _print_bad_response(response)
        return

    click.echo("Product updated successfully!")


@api.command()
@click.option(
    "--type",
    required=True,
    help="The type of the product to create.",
)
@click.argument(
    "product",
    nargs=-1,
    callback=_args_to_dict,
)
def add_product(type: str, product: dict[str, str]):
    """
    Add a new product with the specified type and fields.
    Field arguments are specified as described, with a space between: 'name=value'
    """

    # TODO: perhaps check that these fields are correct before sending?

    body = {"Type": type, "Product": product}
    response = requests.post(f"{URL_BASE}/api/product", json=body)
    if response.status_code != 200:
        _print_bad_response(response)
        return

    click.echo("Product added successfully!")


@api.command()
@click.option(
    "--id",
    required=True,
    help="The ID of the product to delete.",
)
def delete_product(id: str | None):
    """
    Deletes the product specified by the ID.
    """

    response = requests.delete(f"{URL_BASE}/api/product/{id}")
    if response.status_code != 200:
        _print_bad_response(response)

    click.echo("Product deleted successfully!")
