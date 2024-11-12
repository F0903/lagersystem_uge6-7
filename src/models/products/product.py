# classes detailing products in the storage system

from dataclasses import dataclass
import datetime


@dataclass(kw_only=True)
class ProductDescriptor:
    """
    Dataclass that holds the most basic information about every product.
    """

    ID: int  # Handled by SQL
    Name: str
    Description: str
    Quantity: int  # in storage / in stock
    Price: float
    CreatedAt: datetime.datetime  # Handled by SQL
    LastUpdatedAt: datetime.datetime  # Handled by SQL


@dataclass(kw_only=True)
class Product:
    Descriptor: ProductDescriptor
