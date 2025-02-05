<script lang="ts">
	import IconFunnel from '~icons/ion/funnel-sharp';
	import IconAdd from '~icons/ion/add-circle-sharp';

	import { taxonomicRanks, taxons } from '$lib/data/data.svelte';

	// Props
	interface Props {
		classification: Record<string, string>;
	}

	const { classification }: Props = $props();
</script>

<div class="flex flex-wrap gap-2">
	{#each Object.entries(classification) as [taxon, value]}
		<div class="flex w-full gap-3 rounded-full bg-gray-950/20 py-1 pr-1 pl-3">
			<div class="flex w-full items-center justify-between">
				<div class="flex flex-col">
					<span class="text-2xs font-semibold capitalize">{taxon}</span>
					<span class="text-sm capitalize">{value}</span>
				</div>
				<div class="flex flex-col items-end">
					<span class="text-2xs font-semibold capitalize">{taxonomicRanks[taxon]}</span>
					<span class="text-sm capitalize">{taxons[value] ?? 'Error'}</span>
				</div>
			</div>
			<button
				class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500 print:hidden"
				title="Add as filter"
			>
				<IconFunnel class="mt-2 -ml-1 h-5 w-5" />
				<div class="absolute top-2.5 right-2 rounded-full bg-gray-50">
					<IconAdd class="h-4 w-4" />
				</div>
			</button>
		</div>
	{/each}
</div>
