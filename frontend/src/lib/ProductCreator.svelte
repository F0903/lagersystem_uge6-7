<script lang="ts">
    import { addSingleProduct } from "./api";
    import {
        getAttributesOfProductType,
        product_types,
        Product,
    } from "./models/Product";
    import { faPlus, faArrowRight } from "@fortawesome/free-solid-svg-icons";
    import IconButton from "./IconButton.svelte";
    import Dropdown from "../Dropdown.svelte";
    import { findParentWithTag } from "./dom_utils";

    let { addProductCallback }: { addProductCallback: () => Promise<void> } =
        $props();

    let creatorExpanded = $state(false);
    let selectedType = $state("");

    function onCreatorButtonClick() {
        creatorExpanded = !creatorExpanded;
    }

    async function submit(event: Event) {
        let target = event.target as HTMLElement;

        console.log(target);

        let form = findParentWithTag("form", target);

        // Construct form data from the form html element.
        const formData = new FormData(form as HTMLFormElement);
        console.log(formData);

        // Get the entries in the form data wrapped in an object, so we can serialize it to JSON correctly
        const productEntries = Object.fromEntries(
            formData,
        ) as unknown as Product; // This is a little hacky, but we know that we only add valid fields beforehand.

        await addSingleProduct(productEntries, selectedType);
        await addProductCallback();
    }
</script>

<div class="creator-container" class:expanded={creatorExpanded}>
    <IconButton
        custom_class="creator-button"
        click_toggle_class="enabled"
        margin="25px"
        fa_icon={faPlus}
        onclick={onCreatorButtonClick}
    />
    {#if creatorExpanded}
        <div class="creator">
            {#snippet dropdown_content()}
                {#each product_types as productType}
                    <option value={productType}>{productType}</option>
                {/each}
            {/snippet}
            <Dropdown
                name="Type"
                placeholder="Select Type"
                {dropdown_content}
                bind:selected_value={selectedType}
            />

            <form class="creator-form">
                {#if selectedType}
                    <div class="creator-form-inputs">
                        {#each getAttributesOfProductType(selectedType) as attr_name}
                            <label for={attr_name}>{attr_name}</label>
                            <input type="text" name={attr_name} />
                        {/each}
                    </div>
                    <IconButton
                        fa_icon={faArrowRight}
                        onclick={submit}
                        margin="5px"
                    />
                {/if}
            </form>
        </div>
    {/if}
</div>

<style>
    .creator {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    /* Custom class for the creator button */
    :global(.creator-button.enabled) {
        rotate: 45deg;
    }

    .creator-form {
        display: flex;
        flex-direction: column;
        gap: 5px;
        justify-content: center;
        align-items: center;
    }

    .creator-form-inputs {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .creator-container {
        margin: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
