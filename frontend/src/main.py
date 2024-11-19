import click
import requests
from .utils import _args_to_dict

HOST = "localhost"
PORT = 5000
URL_BASE = f"http://{HOST}:{PORT}"


def _print_error(response):
    click.echo(
        f"Error. Response was not 200 (OK). \nResponse was: {response.status_code}\n{response.content}",
        err=True,
    )


@click.group("api")
def api():
    pass


@api.command()
@click.option(
    "--filter",
    help="Filter for product type.",
)
def get_products(filter: str | None):
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
    response = requests.get(f"{URL_BASE}/api/product/{id}")
    if response.status_code != 200:
        _print_error(response)
        return
    product = response.json()
    click.echo(product)


@api.command()
@click.option(
    "--id",
    required=True,
    help="The ID of the product to set.",
)
@click.argument(
    "product",
    nargs=-1,
    callback=_args_to_dict,
)
def set_product(id: str, product_fields: dict[str, str]):
    # TODO: get the product first from the server, then modify the fields with the ones in 'product_fields'
    pass


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
    # TODO: perhaps check that these fields are correct before sending?
    body = {"Type": type, "Product": product}
    response = requests.post(f"{URL_BASE}/api/product", json=body)
    if response.status_code != 200:
        _print_error(response)
        return
    click.echo("Success!")


@api.command()
@click.option(
    "--id",
)
def delete_product(id: str | None):
    pass


if __name__ == "__main__":
    api()
