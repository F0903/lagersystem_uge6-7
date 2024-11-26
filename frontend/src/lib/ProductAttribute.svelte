<script lang="ts">
    let {
        attribute = $bindable(),
        editable,
    }: { attribute: Attribute; editable: boolean } = $props();

    function onValueBlur(event: FocusEvent) {
        const target = event.target as HTMLElement;
        const value = target.textContent;

        if (value === null) {
            console.error("value was null");
            return;
        }

        attribute.Value = value;
    }
</script>

<div class="attr-container" class:editable>
    <span class="attr-name">
        {attribute.Name}:
    </span><br />
    <span class="attr-value" contenteditable={editable} onblur={onValueBlur}>
        {attribute.Value}
    </span>
</div>

<style>
    .attr-value {
        min-height: 20px;
    }
    .attr-container.editable {
        border: 2px dashed var(--secondary-color);
    }
    .attr-container {
        background-color: var(--tertiary-color);
        margin: 5px 0px;
        padding: 10px;
    }

    span {
        font-size: 1.2em;
    }
</style>
