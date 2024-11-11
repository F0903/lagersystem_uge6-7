# class doing administrative tasks on our products

import models.product as m

# what we want the code to do (methods):
#   add a new product (factory class)
#   get products given id
#   modify a product by id
#   delete a product by id

class ProductManager:

    # factory design pattern to create new products
    # lending from https://realpython.com/factory-method-python/#introducing-factory-method
    def create_product(self, type, args): # args for the specific product type. probably should be kwargs or whatever
        creator = self._get_creator(type)
        return creator(self, args) # or kwargs
        
    def _get_creator(self, type):
        if type == 'Clothes':
            return self._create_clothes
        else:
            raise ValueError(type) # idk
        
    def _create_clothes(self, args):
        m.Clothes(args)



    pass