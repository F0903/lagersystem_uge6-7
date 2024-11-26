<script lang="ts">
    import ProductsWidget from "$lib/ProductsWidget.svelte";
</script>

<h1 class="page-title">Lagerstyring</h1>
<div class="widgets">
    <ProductsWidget />
</div>

<style>
    .widgets {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;

        justify-content: center;
    }

    .page-title {
        text-align: center;
    }

    :root {
        --primary-color: #10141b;
        --secondary-color: #202636;
        --tertiary-color: #0c101f;
        --quaternary-color: #dce0d9;

        --primary-text-color: var(--quaternary-color);

        background-color: var(--primary-color);
        color: var(--primary-text-color);
    }
</style>
