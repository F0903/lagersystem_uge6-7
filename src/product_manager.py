# class doing administrative tasks on our products

import models.product as p
from db.db import Db

# TODO
class ProductManager:

    # TODO this is pseudo-code-y right now
    # factory design pattern to create new products
    # lending from https://realpython.com/factory-method-python/#introducing-factory-method
    def new_product(self, type):
        """
        Returns a new, empty instance of a product of the given type.
        """
        creator = self._get_creator(type)
        return creator(self)
        
    def _get_creator(self, type):
        if type == 'Clothing':
            return self._create_clothing
        elif type == 'Book':
            return self._create_book
        else:
            raise ValueError(type) # idk
        
    def _create_clothing(self):
        p.Clothing()

    def _create_book(self):
        p.Book()
    ###

    # basic database operations:

    def add_product(self, product):
        """
        Add a product to the database
        """
        # get database connection
        db = Db()

        # make product object query-able

        # send query to database
        pass

    def get_product(self, id):
        """
        Retrieve a product from the database
        """
        # construct query with id

        # query database
        pass

    # TODO: does this one make sense?
    def modify_product(self, id, product):
        """
        Modify existing product in the database.
        Overwrites the product with ID (id) with the new product object.
        """
        pass

    def delete_product(self, id):
        """
        Delete a product from the database
        """
        # construct query with id

        # query database
        pass


    # others?:

    def get_products(self, of_type):
        pass


    pass