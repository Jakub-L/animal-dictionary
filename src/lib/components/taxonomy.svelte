<script lang="ts">
	import { taxonomicRanks, taxons, taxonFilters } from '$lib/data/state.svelte';
	import Icon from './icon.svelte';

	// Props
	interface Props {
		classification: Record<string, string>;
	}

	const { classification }: Props = $props();

	// Handlers
	const toggleFilter = (taxon: string, value: string) => {
		taxonFilters.value[taxon] = taxonFilters.value[taxon] === value ? '' : value;
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
				class={[
					'relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500',
					taxonFilters.value[taxon] === value &&
						'foucs-visible:outline-red-400 border-red-400 text-red-700 opacity-80 hover:bg-red-400 active:bg-red-500'
				]}
				title={taxonFilters.value[taxon] === value ? 'Remove from filters' : 'Add as filter'}
				onclick={() => toggleFilter(taxon, value)}
			>
				<Icon
					class="h-7 w-7"
					id={taxonFilters.value[taxon] === value ? 'filter-remove' : 'filter-add'}
					alt=""
				/>
			</button>
		</div>
	{/each}
</div>
