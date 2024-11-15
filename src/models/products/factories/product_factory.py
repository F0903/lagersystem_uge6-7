import dataclasses
from typing import Any

from ... import products


# TODO move to product as class methods?


def _get_product_class_dynamically(type: str):
    """
    Dynamically get the class type by name from the products module.
    So for example, if the "type" string is "Clothing", it will return
    the Clothing type.
    """

    product_class = getattr(products, type)
    return product_class


def create_product_from_descriptor(
    descriptor: products.ProductDescriptor, **extra_attributes
) -> products.Product:
    """
    Dynamically get the product class from the "products" module by class name.

    'extra_attributes' represents the additional arguments provided to the constructor of the class.

    Returns:
        The new product instance.
    """

    try:
        type = descriptor.Type
        product_class = _get_product_class_dynamically(type)
        product_instance = product_class(Descriptor=descriptor, **extra_attributes)

        return product_instance
    except AttributeError:
        raise ValueError(f"Unknown product type")


def create_product_from_dict(dict: dict[str, Any]) -> products.Product:
    """
    Create the product dynamically fron a dictionary of fields.

    Requires that it matches an existing product type.
    """

    descriptor_dict = dict["Descriptor"]
    descriptor = products.ProductDescriptor.create_from_dict(descriptor_dict)

    # TODO: perhaps validate the keys in the dict?

    # Get all other props in the dict that isn't "Descriptor"
    other_props = {key: value for key, value in dict.items() if key != "Descriptor"}

    product = create_product_from_descriptor(descriptor, **other_props)

    return product
