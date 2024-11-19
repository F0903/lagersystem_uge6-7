import click
import requests

HOST = "localhost"
PORT = 5000
URL_BASE = f"http://{HOST}:{PORT}"


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
    response = requests.get(URL_BASE + "/api/products", params=filter_query)
    body = response.json()
    click.echo(body)


@api.command()
@click.option(
    "--id",
)
def get_product(id: str | None):
    pass


@api.command()
@click.option(
    "--id",
)
def set_product(id: str | None):
    pass


@api.command()
def add_product():
    pass


@api.command()
@click.option(
    "--id",
)
def delete_product(id: str | None):
    pass


if __name__ == "__main__":
    api()
