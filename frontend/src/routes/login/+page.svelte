<script lang="ts">
    import { enhance } from "$app/forms";
    import { goto } from "$app/navigation";
    import { login } from "$lib/api/auth_api";
    import IconButton from "$lib/IconButton.svelte";
    import type { User } from "$lib/models/User";
    import {
        findParentWithTag,
        getObjectFromFormData,
    } from "$lib/utils/dom_utils";
    import { faArrowRight } from "@fortawesome/free-solid-svg-icons";

    let error: Error | undefined = $state();

    async function submit(event: Event) {
        event.preventDefault();

        error = undefined;

        let form = findParentWithTag("form", event.target as HTMLElement);
        const user = getObjectFromFormData<User>(form as HTMLFormElement);

        try {
            await login(user);
            await goto("/", { invalidateAll: true });
        } catch (err) {
            error = err as Error;
        }
    }
</script>

<div class="login-container">
    <form class="creator-form" action="">
        <label for="Username">Username</label>
        <input type="text" name="Username" />
        <label for="Password">Password</label>
        <input type="password" name="Password" />
        <IconButton fa_icon={faArrowRight} onclick={submit} margin="5px" />
    </form>
    {#if error}
        <div class="login-error">
            <h2>Error!</h2>
            <p>{error.message}</p>
        </div>
    {/if}
</div>

<style>
    .creator-form {
        display: flex;
        flex-direction: column;
        max-width: 20%;
        gap: 15px;
        justify-content: center;
        align-items: center;
    }

    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;

        width: 100%;
        height: 100%;

        margin-top: 20vh;
    }
</style>
