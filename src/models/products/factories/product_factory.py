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
            product_class = getattr(products, type)
            return product_class(Descriptor=descriptor, **extra_attributes)
        except AttributeError:
            raise ValueError(f"Unknown product type: {type}")
