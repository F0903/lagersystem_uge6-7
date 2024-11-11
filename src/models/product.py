# classes detailing products in the storage system

from dataclasses import dataclass
import datetime


@dataclass
class Product: # abstract?
    ID: int # product ID
    Name: str
    Description: str
    Quantity: int # in storage / in stock
    Price: float
    CreatedAt: datetime.datetime


# for example
class Clothing(Product):
    Material: str # could be an enum clothes_materials = Cotton, Polyester, etc etc
    Size: str
    Color: str

# for example 2
class Book(Product):
    Genre: str