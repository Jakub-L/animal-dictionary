<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	import IconSearch from '~icons/ion/search';
	import IconMenu from '~icons/ion/menu';
	import IconClose from '~icons/ion/close';
	import IconShuffle from '~icons/ion/shuffle';
	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';

	import { animals, filteredAnimals } from '$lib/data/state.svelte';
	import { slide } from 'svelte/transition';

	import { sortAnimals } from '$lib/utils';

	// State
	let filterQuery = $state('');
	let menuOpen = $state(false);
	let ordering = $state('en');

	// Utils
	const filterAnimals = () => {
		filteredAnimals.value = animals.filter((animal) =>
			[animal.englishName, animal.latinName, animal.polishName]
				.map((s) => s.toLowerCase())
				.some((s) => s.includes(filterQuery))
		);
	};

	// Handlers
	const handleFilterQuery = (event: Event) => {
		filterQuery = (event.target as HTMLInputElement).value.toLowerCase();
		filterAnimals();
	};

	const handleMenuClose = () => {
		if (!menuOpen) menuOpen = true;
		else {
			filteredAnimals.value = sortAnimals(filteredAnimals.value, ordering);
			menuOpen = false;
		}
	};

	const handleSortChange = (value: string | undefined) => {
		if (!value) return;
		ordering = value;
		handleMenuClose();
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
	<DropdownMenu.Root closeOnItemClick={false} open={menuOpen}>
		<DropdownMenu.Trigger
			class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
			onclick={handleMenuClose}
		>
			<IconClose class={['h-8 w-8', !menuOpen && 'hidden']} />
			<IconMenu class={['h-8 w-8', menuOpen && 'hidden']} />
		</DropdownMenu.Trigger>
		<DropdownMenu.Content class="mt-4 -ml-2 flex w-dvw bg-gray-50 p-4" transition={slide}>
			<div class="grid w-full grid-cols-3">
				<span class="col-span-3 text-xs">Order</span>
				<DropdownMenu.RadioGroup
					onValueChange={handleSortChange}
					value={ordering}
					class="col-span-2 grid h-12 grow grid-cols-2"
				>
					<DropdownMenu.RadioItem
						class={[
							'flex items-center justify-center gap-2 rounded-l-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 saturate-0 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500',
							ordering === 'en' && 'bg-gray-400 saturate-100'
						]}
						value="en"
					>
						<IconGb class="h-5 w-5" />
						English
					</DropdownMenu.RadioItem>
					<DropdownMenu.RadioItem
						class={[
							'flex items-center justify-center gap-2 border border-gray-400 bg-gray-50 p-0.5 text-gray-700 saturate-0 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500',
							ordering === 'pl' && 'bg-gray-400 saturate-100'
						]}
						value="pl"
					>
						<IconPl class="h-5 w-5" />
						Polish
					</DropdownMenu.RadioItem>
				</DropdownMenu.RadioGroup>
				<button
					onclick={() => handleSortChange('rand')}
					class="flex items-center justify-center gap-2 rounded-r-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
				>
					<IconShuffle class="h-5 w-5" />
					Shuffle
				</button>
			</div>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
</div>
