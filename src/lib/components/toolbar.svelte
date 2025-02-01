<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	import IconSearch from '~icons/ion/search';
	import IconMenu from '~icons/ion/menu';

	import { animals, filteredAnimals } from '$lib/data/data.svelte';

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

<div class="my-4 flex h-12 justify-between gap-2 px-2">
	<div class="relative flex h-full grow items-center">
		<input
			class="h-full w-full rounded-full bg-gray-50 py-1 pl-8 text-lg placeholder:text-sm focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400"
			value={filterQuery}
			oninput={handleFilterQuery}
			placeholder="Search by Polish, English or Latin name..."
		/>
		<IconSearch class="absolute left-2 h-5 w-5 opacity-60" />
	</div>
	<DropdownMenu.Root>
		<DropdownMenu.Trigger
			class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500 md:min-h-8 md:min-w-8 print:hidden"
		>
			<IconMenu class="z-10 h-8 w-8" />
		</DropdownMenu.Trigger>
		<DropdownMenu.Content class="w-full bg-gray-50">Hello</DropdownMenu.Content>
	</DropdownMenu.Root>
</div>
