<script lang="ts">
	import IconFunnel from '~icons/ion/funnel-sharp';
	import IconRemove from '~icons/ion/remove-sharp';

	import { taxonomicRanks, taxons, taxonFilters } from '$lib/data/state.svelte';

	// Props
	interface Props {
		classification: Record<string, string>;
	}

	const { classification }: Props = $props();

	// Handlers
	const toggleFilter = (taxon: string, value: string) => {
		if (taxonFilters.value[taxon] === value) taxonFilters.value[taxon] = undefined;
		else taxonFilters.value[taxon] = value;
	};
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
				class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
				title="Add as filter"
				onclick={() => toggleFilter(taxon, value)}
			>
				{#if taxonFilters.value[taxon] === value}
					<IconRemove class="h-6 w-6" />
				{:else}
					<IconFunnel class="mt-0.5 h-4 w-4" />
				{/if}
			</button>
		</div>
	{/each}
</div>
