import json
import click


def print_bad_response(response):
    click.echo(
        f"Error. Response was not 200 (OK). \nResponse was: {response.status_code}\n{response.content}",
        err=True,
    )


def pretty_print_json(json_dict: dict):
    click.echo(json.dumps(json_dict, indent=2))


def args_to_dict(
    ctx: click.Context, attribute: click.Option, attributes: tuple[str, ...]
) -> dict[str, str]:
    """Click callback that converts attributes specified in the form `key=value` to a
    dictionary"""
    result = {}
    for arg in attributes:
        k, v = arg.split("=")
        if k in result:
            raise click.BadParameter(f"Attribute {k!r} is specified twice")
        result[k] = v

    return result
