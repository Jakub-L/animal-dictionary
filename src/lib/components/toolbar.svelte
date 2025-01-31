<script lang="ts">
	import IconSearch from '~icons/ion/search';

	import { animals, filteredAnimals } from '$lib/data/data.svelte';
	import { throttle } from '$lib/utils';

	// State
	let filterQuery = $state('');

	// Handlers
	const filterAnimals = () => {
		filteredAnimals.value = animals.filter((animal) =>
			[animal.englishName, animal.latinName, animal.polishName]
				.map((s) => s.toLowerCase())
				.some((s) => s.includes(filterQuery))
		);
	};

	const handleFilterQuery = (event: Event) => {
		filterQuery = (event.target as HTMLInputElement).value.toLowerCase();
		filterAnimals();
	};
</script>

<div class="h-14 p-2">
	<div class="relative flex h-full items-center">
		<input
			class="h-full w-full rounded-full bg-gray-50 py-1 pl-8 text-lg"
			value={filterQuery}
			oninput={handleFilterQuery}
		/>
		<IconSearch class="absolute left-2 h-5 w-5 opacity-60" />
	</div>
</div>
