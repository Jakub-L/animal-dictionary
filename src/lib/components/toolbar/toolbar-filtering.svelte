<script lang="ts">
	import { DropdownMenu } from 'bits-ui';
	import Placeholder from '$lib/components/placeholder.svelte';

	import IconRemove from '~icons/ion/trash-bin-outline';

	import { taxonFilters, taxonomicRanks, taxons } from '$lib/data/state.svelte';

	// State
	const hasFilters = $derived(Object.values(taxonFilters.value).some((filters) => filters.length));
</script>

<DropdownMenu.Item>
	<span class="col-span-3 text-xs">Filters</span>
	{#if hasFilters}
		<div class="flex flex-col gap-2 md:flex-row md:flex-wrap">
			{#each Object.entries(taxonFilters.value) as [taxon, filter]}
				{#if filter.length}
					<div class="flex gap-3 rounded-full bg-gray-950/20 py-1 pr-1 pl-3">
						<div class="flex w-full items-center justify-between gap-4">
							<div class="flex flex-col">
								<span class="text-2xs font-semibold capitalize">{taxon}</span>
								<span class="text-sm capitalize">{filter}</span>
							</div>
							<div class="flex flex-col items-end">
								<span class="text-2xs font-semibold capitalize">{taxonomicRanks[taxon]}</span>
								<span class="text-sm capitalize">{taxons[filter] ?? 'Error'}</span>
							</div>
						</div>
						<button
							class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
							title="Remove from filters"
							onclick={() => (taxonFilters.value[taxon] = '')}
						>
							<IconRemove class="h-7 w-7" />
						</button>
					</div>
				{/if}
			{/each}
		</div>
	{:else}
		<Placeholder
			header="No taxonomy filters"
			subheader="Try selecting a taxon from an animal's card"
			containerClass="bg-gray-300"
		/>
	{/if}
</DropdownMenu.Item>
