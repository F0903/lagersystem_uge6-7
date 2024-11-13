import models.products as products


class ProductFactory:
    @staticmethod
    def create_product(
        type: str, descriptor: products.ProductDescriptor, **extra_attributes
    ) -> products.Product:
        """
        Dynamically get the product class from the "products" module by class name.

        Returns:
            The new product instance.
        """

        try:
            # Dynamically get the class type by name from the products module.
            # So for example, if the "type" string is "Clothing", it will return
            # the Clothing type.
            product_class = getattr(products, type)

            # Create an instance of the type we just got.
            product_instance = product_class(Descriptor=descriptor, **extra_attributes)

            return product_instance
        except AttributeError:
            raise ValueError(f"Unknown product type: {type}")
