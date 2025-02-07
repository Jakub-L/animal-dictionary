<script lang="ts">
	import IconSearch from '~icons/ion/search';

	// Props
	interface Props {
		header: string;
		subheader: string;
		containerClass?: string;
	}

	const { header, subheader, containerClass = '' }: Props = $props();
</script>

<div
	class={[
		'flex h-full flex-col items-center justify-center gap-2 rounded-3xl bg-gray-50 p-12 text-center',
		containerClass
	]}
>
	<IconSearch class="mx-auto h-10 w-10 opacity-50" />
	<span class="font-semibold opacity-85">{header}</span>
	<span class="text-sm opacity-85">{subheader}</span>
</div>
