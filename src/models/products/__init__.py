# Module init for easier importing.

from .book import Book
from .clothing import Clothing
from .product import Product, ProductDescriptor
from .factories.product_factory import (
    create_product_from_dict,
    create_product_from_descriptor,
)
