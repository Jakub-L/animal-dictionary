<script lang="ts">
	interface Props {
		id: string;
		class: string;
		alt: string;
	}

	const { id, class: className, alt }: Props = $props();
</script>

<svg role="img" class={className} aria-label={alt} width="32" height="32" viewBox="0 0 32 32">
	<use href={`/icons/${id}.svg#${id}`} />
</svg>
