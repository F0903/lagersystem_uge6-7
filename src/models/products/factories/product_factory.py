from ...products import product


class ProductFactory:
    @staticmethod
    def create_product(
        type: str, descriptor: product.ProductDescriptor, **extra_attributes
    ) -> product.Product:
        """
        Dynamically get the product class from the "products" module by class name.

        Returns:
            The new product instance.
        """
        try:
            product_class = getattr(product, type)
            return product_class(Descriptor=descriptor, **extra_attributes)
        except AttributeError:
            raise ValueError(f"Unknown product type: {type}")


def create_product(
        type: str, descriptor: product.ProductDescriptor, **extra_attributes
    ) -> product.Product:
        """
        Dynamically get the product class from the "products" module by class name.

        Returns:
            The new product instance.
        """
        try:
            product_class = getattr(product, type)
            return product_class(Descriptor=descriptor, **extra_attributes)
        except AttributeError:
            raise ValueError(f"Unknown product type: {type}")