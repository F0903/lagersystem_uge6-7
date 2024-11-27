<script lang="ts">
    import { onMount } from "svelte";
    import { getAllProducts } from "./api";
    import type { DatabaseProduct } from "./models/DatabaseProduct";
    import ProductCard from "./ProductCard.svelte";
    import ProductCreator from "./ProductCreator.svelte";
    import IconButton from "./IconButton.svelte";
    import { faRefresh } from "@fortawesome/free-solid-svg-icons";

    let products: DatabaseProduct[] = $state([]);

    async function loadProducts() {
        console.log("loading products...");
        products = await getAllProducts();
    }

    async function addProductCallback() {
        //TODO: It would probably be better to implement getting the newest product, than to get all of them at once.
        await loadProducts();
    }

    async function refresh() {
        // Completely refresh from scratch
        products = [];
        await loadProducts();
    }

    onMount(async () => {
        await loadProducts();
    });
</script>

<div class="products-widget">
    <header>
        <h2 class="title">Products</h2>
        <IconButton
            fa_icon={faRefresh}
            onclick={refresh}
            size="40px"
            padding="10px"
        />
    </header>

    <div class="products-container">
        {#await products}
            <span>loading...</span>
        {:then products}
            {#each products as db_product}
                <ProductCard {db_product} />
            {/each}
        {/await}
    </div>
    <ProductCreator {addProductCallback} />
</div>

<style>
    header {
        display: flex;
        flex-direction: row;
        gap: 10px;
        place-items: center center;
        justify-content: center;
        margin: 25px;
    }

    .title {
        text-align: center;
        margin: 10px 0px;
    }

    .products-widget {
        background-color: var(--primary-color);
        padding: 20px;
        width: fit-content;
    }

    .products-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
    }
</style>
