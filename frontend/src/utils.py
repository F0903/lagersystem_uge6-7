import click


def _args_to_dict(
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
