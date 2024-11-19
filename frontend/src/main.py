import click
import requests

HOST = "localhost"
PORT = 5000
URL_BASE = f"http://{HOST}:{PORT}"


@click.command()
@click.option("--filter", help="Filter for product type.")
def get_product(filter: str | None):
    response = requests.get(URL_BASE + "/api/products")
    body = response.json()
    print(body)


@click.command()
def set_product():
    pass


if __name__ == "__main__":
    get_product()
