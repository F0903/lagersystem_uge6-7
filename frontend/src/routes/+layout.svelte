<script lang="ts">
    let { children } = $props();
</script>

<header>
    <h1 class="page-title">Lagerstyring</h1>
</header>
{@render children()}

<style>
    .page-title {
        text-align: center;
        margin: 5px;
        font-size: 1.55rem;
    }

    header {
        background-color: var(--secondary-color);
        padding: 10px;
    }

    :global(button:hover) {
        cursor: pointer;
    }

    :global(body) {
        padding: 0;
        margin: 0;
    }

    :root {
        --primary-color: #10141b;
        --secondary-color: #202636;
        --tertiary-color: #0c101f;
        --quaternary-color: #dce0d9;

        --primary-text-color: var(--quaternary-color);

        background-color: var(--primary-color);
        color: var(--primary-text-color);
        font-family: "Roboto Flex Variable", sans-serif;
    }

    /* roboto-flex-latin-wght-normal */
    @font-face {
        font-family: "Roboto Flex Variable";
        font-style: oblique 0deg 10deg;
        font-display: swap;
        font-weight: 100 1000;
        font-stretch: 25% 151%;
        src: url(@fontsource-variable/roboto-flex/files/roboto-flex-latin-full-normal.woff2)
            format("woff2-variations");
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
            U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC,
            U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    /* roboto-flex-latin-ext-wght-normal */
    @font-face {
        font-family: "Roboto Flex Variable";
        font-style: oblique 0deg 10deg;
        font-display: swap;
        font-weight: 100 1000;
        font-stretch: 25% 151%;
        src: url(@fontsource-variable/roboto-flex/files/roboto-flex-latin-ext-full-normal.woff2)
            format("woff2-variations");
        unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F,
            U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F,
            U+A720-A7FF;
    }
</style>
