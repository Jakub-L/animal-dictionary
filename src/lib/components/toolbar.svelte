<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	import IconSearch from '~icons/ion/search';
	import IconMenu from '~icons/ion/menu';
	import IconClose from '~icons/ion/close';
	import IconShuffle from '~icons/ion/shuffle';
	import IconRemove from '~icons/ion/trash-bin-outline';
	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';

	import { nameQuery, ordering, taxonFilters } from '$lib/data/state.svelte';
	import { slide } from 'svelte/transition';

	// State
	let menuOpen = $state(false);
	const hasFilters = $derived(Object.values(taxonFilters.value).some((filters) => filters.length));

	// Handlers
	const handleFilterQuery = (event: Event) => {
		nameQuery.value = (event.target as HTMLInputElement).value.toLowerCase();
	};

	const handleMenuClose = () => {
		menuOpen = !menuOpen;
	};

	const handleSortChange = (value: string | undefined) => {
		if (!value) return;
		ordering.value = value;
		handleMenuClose();
	};
</script>

<div class="my-4 flex h-12 justify-between gap-2 px-2">
	<div class="relative flex h-full grow items-center">
		<input
			class="h-full w-full rounded-full bg-gray-50 py-1 pl-8 text-lg placeholder:text-sm focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400"
			value={nameQuery.value}
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
		<DropdownMenu.Content
			class="mt-4 -ml-2 flex w-dvw flex-col gap-6 bg-gray-50 p-4"
			transition={slide}
		>
			<div class="grid w-full grid-cols-3">
				<span class="col-span-3 text-xs">Order</span>
				<DropdownMenu.RadioGroup
					onValueChange={handleSortChange}
					value={ordering.value}
					class="col-span-2 grid h-12 grow grid-cols-2"
				>
					<DropdownMenu.RadioItem
						class={[
							'flex items-center justify-center gap-2 rounded-l-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 saturate-0 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500',
							ordering.value === 'en' && 'bg-gray-400 saturate-100'
						]}
						value="en"
					>
						<IconGb class="h-5 w-5" />
						English
					</DropdownMenu.RadioItem>
					<DropdownMenu.RadioItem
						class={[
							'flex items-center justify-center gap-2 border border-gray-400 bg-gray-50 p-0.5 text-gray-700 saturate-0 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500',
							ordering.value === 'pl' && 'bg-gray-400 saturate-100'
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
			<DropdownMenu.Item>
				<span class="col-span-3 text-xs">Filters</span>
				{#if hasFilters}
					{#each Object.entries(taxonFilters.value) as [taxon, filters]}
						{#if filters.length}
							<div class="flex w-full gap-3 rounded-full bg-gray-950/20 py-1 pr-1 pl-3">
								<span>{taxon}</span>
								<span>{filters.join(', ')}</span>
								<button
									class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
									title="Remove from filters"
									onclick={() => (taxonFilters.value[taxon] = [])}
								>
									<IconRemove class="h-6 w-6" />
								</button>
							</div>
						{/if}
					{/each}
				{:else}
					<div
						class=" flex h-full flex-col items-center justify-center gap-2 rounded-3xl bg-gray-300 p-4 text-center"
					>
						<IconSearch class="mx-auto h-10 w-10 opacity-50" />
						<span class="font-semibold opacity-85">No taxonomy filters</span>
						<span class="text-sm opacity-85">Try selecting a taxon from an animal's card</span>
					</div>
				{/if}
			</DropdownMenu.Item>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
</div>
