import { PUBLIC_BACKEND_URL } from "$env/static/public";
import type { User } from "$lib/models/User";

export class InvalidCredsError extends Error {}

export async function login(user: User) {
    const resp = await fetch(`${PUBLIC_BACKEND_URL}/api/login`, {
        method: "POST",
        body: JSON.stringify(user),
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include",
    });

    if (!resp.ok) {
        switch (resp.status) {
            case 401:
                throw new InvalidCredsError(`Invalid username or password`);
            default:
                throw new Error(
                    `Response was not OK. Response was:\n${resp.statusText}`
                );
        }
    }
}
