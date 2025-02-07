<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	import IconShuffle from '~icons/ion/shuffle';
	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';

	import { ordering } from '$lib/data/state.svelte';

	// Handlers
	const handleSortChange = (value: string | undefined) => {
		if (!value) return;
		ordering.value = value;
	};
</script>

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
