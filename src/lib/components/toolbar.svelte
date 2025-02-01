<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	import IconSearch from '~icons/ion/search';
	import IconMenu from '~icons/ion/menu';
	import IconClose from '~icons/ion/close';

	import { animals, filteredAnimals } from '$lib/data/data.svelte';
	import { slide } from 'svelte/transition';

	// State
	let filterQuery = $state('');
	let menuOpen = $state(false);
	let ordering = $state('en');

	// Utils
	const stripString = (s: string) => s.toLowerCase().replace(/[^a-ząęóćńśźżł ]/g, '');

	const getSubstringAt = (s: string, i: number) => {
		return stripString(s).split(' ').at(i) ?? '';
	};

	function shuffleArray(arr: any[]) {
		for (let i = arr.length - 1; i >= 1; i--) {
			const j = Math.floor(Math.random() * (i + 1));
			[arr[i], arr[j]] = [arr[j], arr[i]];
		}
	}

	const filterAnimals = () => {
		filteredAnimals.value = animals.filter((animal) =>
			[animal.englishName, animal.latinName, animal.polishName]
				.map((s) => s.toLowerCase())
				.some((s) => s.includes(filterQuery))
		);
	};

	const sortAnimals = () => {
		if (ordering === 'en') {
			filteredAnimals.value.sort((a, b) =>
				getSubstringAt(a.englishName, -1).localeCompare(getSubstringAt(b.englishName, -1), 'en')
			);
		} else if (ordering === 'pl') {
			filteredAnimals.value.sort((a, b) =>
				getSubstringAt(a.polishName, 0).localeCompare(getSubstringAt(b.polishName, 0), 'pl')
			);
		} else {
			shuffleArray(filteredAnimals.value);
		}
	};

	// Handlers
	const handleFilterQuery = (event: Event) => {
		filterQuery = (event.target as HTMLInputElement).value.toLowerCase();
		filterAnimals();
	};

	const handleMenuClose = () => {
		if (!menuOpen) menuOpen = true;
		else {
			sortAnimals();
			menuOpen = false;
		}
	};

	const handleSortChange = (value: string | undefined) => {
		console.log(value);
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
			class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500 md:min-h-8 md:min-w-8 print:hidden"
			onclick={handleMenuClose}
		>
			<IconClose class={['h-8 w-8', !menuOpen && 'hidden']} />
			<IconMenu class={['h-8 w-8', menuOpen && 'hidden']} />
		</DropdownMenu.Trigger>
		<DropdownMenu.Content class="mt-4 -ml-2 flex w-dvw bg-gray-50 p-4" transition={slide}>
			<div class="grid w-full grid-cols-3">
				<DropdownMenu.RadioGroup
					onValueChange={handleSortChange}
					value={ordering}
					class="col-span-2 grid grow grid-cols-2"
				>
					<DropdownMenu.RadioItem
						class="flex justify-center rounded-l-full border border-gray-400"
						value="en">EN</DropdownMenu.RadioItem
					>
					<DropdownMenu.RadioItem class="flex justify-center border border-gray-400" value="pl"
						>PL</DropdownMenu.RadioItem
					>
				</DropdownMenu.RadioGroup>
				<button
					onclick={() => handleSortChange('rand')}
					class="rounded-r-full border border-gray-400">Rand</button
				>
			</div>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
</div>
