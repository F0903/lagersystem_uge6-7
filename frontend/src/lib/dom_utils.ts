export function findParentWithTag(
    tag: string,
    elem: HTMLElement
): HTMLElement | null {
    console.log(elem.tagName);
    if (elem.tagName.toLowerCase() === tag) {
        return elem;
    }

    const parent = elem.parentElement;
    if (!parent) {
        return null;
    }
    return findParentWithTag(tag, parent);
}
