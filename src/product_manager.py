# class doing administrative tasks on our products

import models.product as p

# what we want the code to do (methods):
#   add a new product (factory class)
#   get products by id
#   modify a product by id
#   delete a product by id

# TODO
class ProductManager:

    # TODO this is pseudo-code-y right now
    # factory design pattern to create new products
    # lending from https://realpython.com/factory-method-python/#introducing-factory-method
    def add_product(self, type, args): # args for the specific product type. probably should be kwargs or whatever
        creator = self._get_creator(type)
        return creator(self, args) # or kwargs
        
    def _get_creator(self, type):
        if type == 'Clothes':
            return self._create_clothes
        elif type == 'Books':
            return self._create_books
        else:
            raise ValueError(type) # idk
        
    def _create_clothes(self, args):
        p.Clothing(args)

    def _create_books(self, args):
        p.Book(args)
    ###

    # basic operations:

    def get_product(self, id):
        pass

    def modify_product(self, id):
        pass

    def delete_product(self, id):
        pass


    # others:

    def get_products(self, of_type):
        pass


    pass