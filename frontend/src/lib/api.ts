import { PUBLIC_BACKEND_URL } from "$env/static/public";
import type { DatabaseProduct } from "./models/DatabaseProduct";
import type { Product } from "./models/Product";

export async function getAllProducts(): Promise<DatabaseProduct[]> {
    const resp = await fetch(`${PUBLIC_BACKEND_URL}/api/products`);
    if (!resp.ok) {
        throw new Error(
            `Response was not OK. Response was:\n${resp.statusText}`
        );
    }

    const products = await resp.json();
    let dbProducts: DatabaseProduct[] = [];
    products.forEach((dbProduct: DatabaseProduct) => {
        dbProducts.push(dbProduct);
    });

    return dbProducts;
}

export async function getSingleProduct(id: number): Promise<DatabaseProduct> {
    const resp = await fetch(`${PUBLIC_BACKEND_URL}/api/product/${id}`);
    if (!resp.ok) {
        throw new Error(
            `Response was not OK. Response was:\n${resp.statusText}`
        );
    }

    // The API always wraps it in an array.
    const products = await resp.json();
    const product = products[0];

    return product;
}

export async function setSingleProduct(
    id: number,
    product: Product,
    product_type: string
) {
    // Create an object that has both the product and type string as needed by the API.
    const productTypePair: { Type: string; Product: Product } = {
        Type: product_type,
        Product: product,
    };

    const resp = await fetch(`${PUBLIC_BACKEND_URL}/api/product/${id}`, {
        method: "PUT",
        body: JSON.stringify(productTypePair),
        headers: {
            "Content-Type": "application/json",
        },
    });
    if (!resp.ok) {
        throw new Error(
            `Response was not OK. Response was:\n${resp.statusText}`
        );
    }
}

export async function addSingleProduct(product: Product, product_type: string) {
    // Create an object that has both the product and type string as needed by the API.
    const productTypePair: { Type: string; Product: Product } = {
        Type: product_type,
        Product: product,
    };

    const resp = await fetch(`${PUBLIC_BACKEND_URL}/api/product`, {
        method: "POST",
        body: JSON.stringify(productTypePair),
        headers: {
            "Content-Type": "application/json",
        },
    });
    if (!resp.ok) {
        throw new Error(
            `Response was not OK. Response was:\n${resp.statusText}`
        );
    }
}

export async function deleteSingleProduct(id: number) {
    const resp = await fetch(`${PUBLIC_BACKEND_URL}/api/product/${id}`, {
        method: "DELETE",
    });
    if (!resp.ok) {
        throw new Error(
            `Response was not OK. Response was:\n${resp.statusText}`
        );
    }
}
