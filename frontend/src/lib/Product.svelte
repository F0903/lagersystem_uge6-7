<script lang="ts">
    import { deleteSingleProduct, setSingleProduct } from "./api";
    import type { DatabaseProduct } from "./models/DatabaseProduct";
    import ProductAttribute from "./ProductAttribute.svelte";

    let { db_product }: { db_product: DatabaseProduct } = $props();

    const descriptor = db_product.Descriptor;
    const product = $state(db_product.Product);

    // Create attributes objects from each property on product.
    let attributes: Attribute[] = $state([]);
    Object.entries(product).forEach((attribute) => {
        attributes.push({ Name: attribute[0], Value: attribute[1] });
    });

    let oldAttributes: Attribute[] = [];

    let editable = $state(false);

    async function deleteSelf() {
        await deleteSingleProduct(descriptor.ID);
        htmlRoot.remove();
    }

    async function startEditing() {
        oldAttributes = $state.snapshot(attributes);
        editable = true;
    }

    async function saveEdits() {
        editable = false;
        console.log(attributes);
        console.log(oldAttributes);
        console.log(product);
    }

    async function discardEdits() {
        editable = false;
        console.log(attributes);
        attributes = oldAttributes;
        console.log(oldAttributes);
        console.log(attributes);
    }

    let htmlRoot: HTMLElement;
</script>

<div class="product" bind:this={htmlRoot}>
    {#each attributes as _, i}
        <ProductAttribute bind:attribute={attributes[i]} {editable} />
    {/each}
    <div class="descriptor-section">
        <span>ID: {descriptor.ID}</span>
        <span>Type: {descriptor.Type}</span>
        <span>Created at: {descriptor.CreatedAt}</span>
        <span>Last updated at: {descriptor.LastUpdatedAt}</span>
    </div>
    <div class="buttons">
        <button onclick={deleteSelf}>Delete</button>
        {#if editable}
            <button onclick={saveEdits}>Save Changes</button>
            <button onclick={discardEdits}>Discard Changes</button>
        {:else}
            <button onclick={startEditing}>Edit</button>
        {/if}
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
