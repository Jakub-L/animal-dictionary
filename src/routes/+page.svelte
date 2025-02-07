<script lang="ts">
	import '../app.css';

	import type { Animal } from '$lib/types';

	import AnimalCard from '$lib/components/animal-card/animal-card.svelte';
	import Placeholder from '$lib/components/placeholder.svelte';
	import Toolbar from '$lib/components/toolbar.svelte';

	import { animals, ordering, nameQuery, taxonFilters } from '$lib/data/state.svelte';
	import { sortAnimals, filterAnimals } from '$lib/utils';

	const filteredAnimals: Animal[] = $derived(
		sortAnimals(filterAnimals(animals, nameQuery.value, taxonFilters.value), ordering.value)
	);
</script>

<div class="flex h-full flex-col">
	<Toolbar />
	<div class="flex h-full flex-col items-center gap-4 overflow-y-auto px-2">
		{#if filteredAnimals.length === 0}
			<Placeholder header="No animals found" subheader="Try changing the search query or filters" />
		{/if}
		{#each filteredAnimals as animal}
			<AnimalCard {animal} />
		{/each}
	</div>
</div>
