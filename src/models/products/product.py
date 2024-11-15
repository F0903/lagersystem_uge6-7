# classes detailing products in the storage system

from dataclasses import dataclass
import datetime
from typing import Any, Self


# A smarter method of doing this would probably be
# using properties instead of docstring warnings,
# but would also be more complex, so alas
@dataclass(kw_only=True)
class ProductDescriptor:
    """
    Dataclass that holds the most basic information about every product.
    """

    ID: int
    """**(DO NOT SET MANUALLY)** Handled by SQL """

    Type: str
    """**(DO NOT SET MANUALLY)** The type string, which is currently the name of the dataclass it's assocaited with."""

    Name: str
    Description: str
    Quantity: int  # in storage / in stock
    Price: float

    CreatedAt: datetime.datetime
    """**(DO NOT SET MANUALLY)** The date at which this record was created in the database. Handled by SQL"""

    LastUpdatedAt: datetime.datetime
    """**(DO NOT SET MANUALLY)** The date at which this record was updated in the database. Handled by SQL"""

    @classmethod
    def create_from_dict(cls, dict: dict[str, Any]) -> Self:
        """
        Factory method for creating a ProductDescriptor from a dictionary.
        """

        descriptor = cls(
            ID=dict["ID"],
            Type=dict["Type"],
            Name=dict["Name"],
            Description=dict["Description"],
            Quantity=dict["Quantity"],
            Price=dict["Price"],
            CreatedAt=dict["CreatedAt"],
            LastUpdatedAt=dict["LastUpdatedAt"],
        )
        return descriptor


@dataclass(kw_only=True)
class Product:
    """
    The base generic product class

    This class only has one field to make it easier to iterate over the fields of the subclasses,
    as only the Descriptor here needs to be ignored to get all the child fields.
    """

    Descriptor: ProductDescriptor
