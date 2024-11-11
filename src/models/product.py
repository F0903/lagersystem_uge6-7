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

    def get_sql_values(self):
        """
        Returns a tuple of the product's fields, minus it's ID
        """
        return (self.Name, self.Description, self.Quantity, self.Price, self.CreatedAt)


# for example
class Clothing(Product):
    Material: str # could be an enum clothes_materials = Cotton, Polyester, etc etc
    Size: str
    Color: str

    def get_sql_values(self):
        """
        Returns a tuple of the product's fields, minus it's ID
        """
        return (*super().get_sql_values(), self.Material, self.Size, self.Color)


# for example 2
class Book(Product):
    Genre: str

    def get_sql_values(self):
        """
        Returns a tuple of the product's fields, minus it's ID
        """
        return (*super().get_sql_values(), self.Genre)
