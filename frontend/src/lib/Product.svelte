<script lang="ts">
    import { deleteSingleProduct } from "./api";
    import type { DatabaseProduct } from "./models/DatabaseProduct";
    import ProductAttribute from "./ProductAttribute.svelte";

    let { db_product }: { db_product: DatabaseProduct } = $props();

    let htmlRoot: HTMLElement;

    const product = db_product.Product;
    const descriptor = db_product.Descriptor;

    const attributes = Object.entries(product);

    async function deleteSelf() {
        await deleteSingleProduct(descriptor.ID);
        htmlRoot.remove();
    }
</script>

<div class="product" bind:this={htmlRoot}>
    {#each attributes as attribute}
        <ProductAttribute
            attribute={{ Name: attribute[0], Value: attribute[1] }}
        />
    {/each}
    <div class="descriptor-section">
        <span>ID: {descriptor.ID}</span>
        <span>Type: {descriptor.Type}</span>
        <span>Created at: {descriptor.CreatedAt}</span>
        <span>Last updated at: {descriptor.LastUpdatedAt}</span>
    </div>
    <div class="buttons">
        <button onclick={deleteSelf}>Delete</button>
    </div>
</div>

<style>
    .buttons {
        height: auto;
        place-self: center end;
    }

    .descriptor-section {
        margin-top: 10px;
        display: flex;
        flex-direction: column;
        gap: 2px;
    }

    .product {
        display: flex;
        flex-direction: column;
        background-color: var(--secondary-color);
        width: fit-content;
        padding: 25px;
        border-radius: 20px;
    }
</style>
