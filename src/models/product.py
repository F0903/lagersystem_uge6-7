# classes detailing products in the storage system

from dataclasses import dataclass
import datetime


@dataclass
class Product: # abstract?
    ID: int = 0 # product ID
    Name: str = ""
    Description: str = ""
    Quantity: int = 0 # in storage / in stock
    Price: float = 0.0
    CreatedAt: datetime.datetime = datetime.datetime.now()

    def get_sql_values(self):
        """
        Returns a tuple of the product's fields, minus it's ID
        """
        t = []
        for k, v in self.__dict__.items():
            if k != "ID":
                t.append(v)
        return tuple(t)


# for example
@dataclass
class Clothing(Product):
    Material: str = '' # could be an enum clothes_materials = Cotton, Polyester, etc etc
    Size: str = ''
    Color: str = ''


# for example 2
@dataclass
class Book(Product):
    Page_count: int = 0
    Genre: str = ""
