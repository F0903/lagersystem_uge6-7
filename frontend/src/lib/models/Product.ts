export const product_types = ["Product", "Clothing", "Book"];

// Try to find a more generic solution for this instead of hardcoding it.
export function getAttributesOfProductType(typ: string) {
    switch (typ) {
        case "Product":
            return Product.getAttributeNames();
        case "Clothing":
            return Clothing.getAttributeNames();
        case "Book":
            return Book.getAttributeNames();
        default:
            throw new Error(`Unknown product type: ${typ}`);
    }
}

export class Product {
    Name!: string;
    Description!: string;
    Price!: string;
    Quantity!: number;

    public static getAttributeNames() {
        return ["Name", "Description", "Price", "Quantity"];
    }
}

export class Clothing extends Product {
    Color!: string;
    Material!: string;
    Size!: string;

    public static getAttributeNames() {
        return [...super.getAttributeNames(), "Color", "Material", "Size"];
    }
}

export class Book extends Product {
    Genre!: string;
    PageCount!: number;

    public static getAttributeNames() {
        return [...super.getAttributeNames(), "Genre", "PageCount"];
    }
}
