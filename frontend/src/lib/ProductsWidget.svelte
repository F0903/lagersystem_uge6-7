<script lang="ts">
    import { onMount } from "svelte";
    import { getAllProducts } from "./api";
    import type { DatabaseProduct } from "./models/DatabaseProduct";
    import Product from "./Product.svelte";
    import ProductCreator from "./ProductCreator.svelte";

    let products: DatabaseProduct[] = $state([]);

    async function loadProducts() {
        console.log("loading products...");
        products = await getAllProducts();
    }

    async function addProductCallback() {
        //TODO: It would probably be better to implement getting the newest product, than to get all of them at once.
        await loadProducts();
    }

    onMount(async () => {
        await loadProducts();
    });
</script>

<div class="products-widget">
    <h2 class="title">Products</h2>
    <button onclick={loadProducts}>Refresh</button>
    <div class="products-container">
        {#await products}
            <span>loading...</span>
        {:then products}
            {#each products as db_product}
                <Product {db_product} />
            {/each}
        {/await}
    </div>
    <ProductCreator {addProductCallback} />
</div>

<style>
    .title {
        text-align: center;
        margin: 10px 0px;
    }

    .products-widget {
        background-color: var(--primary-color);
        padding: 20px;
        border: 2px solid var(--secondary-color);
        border-radius: 25px;
        width: fit-content;
    }

    .products-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 20px;
    }
</style>
