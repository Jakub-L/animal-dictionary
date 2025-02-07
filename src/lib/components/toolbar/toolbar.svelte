<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	import IconSearch from '~icons/ion/search';
	import IconMenu from '~icons/ion/menu';
	import IconClose from '~icons/ion/close';

	import { nameQuery } from '$lib/data/state.svelte';
	import { slide } from 'svelte/transition';
	import ToolbarOrdering from './toolbar-ordering.svelte';
	import ToolbarFiltering from './toolbar-filtering.svelte';

	// State
	let menuOpen = $state(false);

	// Handlers
	const handleFilterQuery = (event: Event) => {
		nameQuery.value = (event.target as HTMLInputElement).value.toLowerCase();
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
	<DropdownMenu.Root closeOnItemClick={false} bind:open={menuOpen}>
		<DropdownMenu.Trigger
			class="relative flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 bg-gray-50 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
		>
			<IconClose class={['h-8 w-8', !menuOpen && 'hidden']} />
			<IconMenu class={['h-8 w-8', menuOpen && 'hidden']} />
		</DropdownMenu.Trigger>
		<DropdownMenu.Content
			class="mt-4 -ml-2 flex w-dvw flex-col gap-6 bg-gray-50 p-4"
			transition={slide}
		>
			<ToolbarOrdering />
			<ToolbarFiltering />
		</DropdownMenu.Content>
	</DropdownMenu.Root>
</div>
