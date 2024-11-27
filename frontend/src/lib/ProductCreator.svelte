<script lang="ts">
    import { addSingleProduct } from "./api";
    import {
        getAttributesOfProductType,
        product_types,
        Product,
    } from "./models/Product";

    let { addProductCallback }: { addProductCallback: () => Promise<void> } =
        $props();

    let creatorExpanded = $state(false);
    let selectedType = $state("");

    function onCreateButtonClick() {
        creatorExpanded = !creatorExpanded;
    }

    async function onSubmit(event: SubmitEvent) {
        event.preventDefault();

        // Construct form data from the form html element.
        const formData = new FormData(event.target as HTMLFormElement);
        console.log(formData);

        // Get the entries in the form data wrapped in an object, so we can serialize it to JSON correctly
        const productEntries = Object.fromEntries(
            formData,
        ) as unknown as Product; // This is a little hacky, but we know that we only add valid fields beforehand.

        await addSingleProduct(productEntries, selectedType);
        await addProductCallback();
    }
</script>

<div class="creator" class:expanded={creatorExpanded}>
    <button class="create-button" onclick={onCreateButtonClick}>+</button>
    {#if creatorExpanded}
        <label for="type-select">Type:</label>
        <select class="type-select" name="Type" bind:value={selectedType}>
            {#each product_types as productType}
                <option value={productType}>{productType}</option>
            {/each}
        </select>
        <form class="creator-form" onsubmit={onSubmit}>
            {#if selectedType}
                <div class="product-placeholder">
                    {#each getAttributesOfProductType(selectedType) as attr_name}
                        <label for={attr_name}>{attr_name}</label>
                        <input type="text" name={attr_name} />
                    {/each}
                </div>
            {/if}
            <input type="submit" value="Submit" />
        </form>
    {/if}
</div>

<style>
    .creator-form {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .product-placeholder {
        display: flex;
        flex-direction: column;
    }

    .creator.expanded .create-button {
        rotate: 45deg;
    }

    .create-button {
        background-color: var(--secondary-color);
        color: var(--primary-text-color);
        border: 0;
        font-size: 3rem;
        margin: 0;
        padding: 10px;
        aspect-ratio: 1/1;
        width: 50px;
        text-align: center;
        line-height: 0px;
        border-radius: 50%;
    }

    .creator {
        margin: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
