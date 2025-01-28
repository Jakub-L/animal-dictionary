<script lang="ts">
	import '../app.css';

	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';
	import IconCaretDown from '~icons/ion/caret-down';
	import IconCaretUp from '~icons/ion/caret-up';

	import { Collapsible } from 'bits-ui';
	import { slide } from 'svelte/transition';

	import { data } from '$lib/data';
</script>

<div class="flex flex-col gap-4 p-4">
	{#each data as animal}
		<div class="flex flex-col gap-2 rounded-3xl bg-gray-50 p-4">
			<img src={animal.imageSrc} alt={animal.latinName} class="rounded-2xl" />
			<h2 class="grid grid-cols-2 items-center">
				<div class="relative flex h-full items-center pr-2 pl-7">
					<IconGb class="absolute left-0 h-5 w-5" />
					<span>{animal.englishName}</span>
				</div>
				<div
					class="relative flex h-full items-center border-l border-gray-950 pr-7 pl-2 text-right"
				>
					<span>{animal.polishName}</span>
					<IconPl class="absolute right-0 h-5 w-5" />
				</div>
			</h2>
			<Collapsible.Root>
				<div class="relative flex h-12 items-center justify-center">
					<span class="text-xs uppercase italic">{animal.latinName}</span>
					<Collapsible.Trigger
						class="group absolute right-0 flex min-h-12 min-w-12 items-center justify-center rounded-full p-0.5 text-gray-700 hover:bg-gray-700/30 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-700/60 md:min-h-8 md:min-w-8 print:hidden"
					>
						<IconCaretDown class="h-5 w-5 group-data-[state=open]:hidden" />
						<IconCaretUp class="h-5 w-5 group-data-[state=closed]:hidden" />
					</Collapsible.Trigger>
				</div>
				<Collapsible.Content transition={slide}>Hello</Collapsible.Content>
			</Collapsible.Root>
		</div>
	{/each}
</div>
