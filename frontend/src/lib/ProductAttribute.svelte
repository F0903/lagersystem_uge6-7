<script lang="ts">
    let { attribute }: { attribute: Attribute } = $props();
</script>

<!-- TODO: make attribute editable -->
<div class="attr-container">
    <span class="name">
        {attribute.Name}:
    </span>
    <span class="value">
        {attribute.Value}
    </span>
</div>

<style>
    .attr-container {
        background-color: var(--tertiary-color);

        margin: 5px 0px;
        padding: 5px;
    }

    span {
        font-size: 1.2em;
    }
</style>
