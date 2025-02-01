<script lang="ts">
	import '../app.css';

	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';
	import IconCaretDown from '~icons/ion/caret-down';
	import IconCaretUp from '~icons/ion/caret-up';
	import IconSearch from '~icons/ion/search';

	import Taxonomy from '$lib/components/taxonomy.svelte';
	import AudioPlayer from '$lib/components/audio-player.svelte';
	import { Collapsible } from 'bits-ui';
	import { slide } from 'svelte/transition';

	import { filteredAnimals } from '$lib/data/data.svelte';
	import Toolbar from '$lib/components/toolbar.svelte';
</script>

{#snippet wikiLink(lang: string, text: string, latinName: string)}
	<a
		class="text-gray-700 underline hover:scale-105 active:scale-95"
		href={`https://${lang}.wikipedia.org/wiki/${latinName}`}
		target="_blank"
		rel="noopener"
	>
		{text}
	</a>
{/snippet}

<div class="flex h-full flex-col">
	<Toolbar />
	<div class="flex h-full flex-col gap-4 overflow-y-auto px-2">
		{#if filteredAnimals.value.length === 0}
			<div
				class=" flex h-full flex-col items-center justify-center gap-2 rounded-3xl bg-gray-50 p-12 text-center"
			>
				<IconSearch class="mx-auto h-10 w-10 opacity-50" />
				<span class="font-semibold opacity-85">No animals found</span>
				<span class="text-sm opacity-85">Try changing the search query or filters</span>
			</div>
		{/if}
		{#each filteredAnimals.value as animal}
			<div class="flex flex-col gap-2 rounded-3xl bg-gray-50 p-4">
				<img src={animal.imageSrc} alt={animal.latinName} class="rounded-2xl" />
				<h2 class="grid grid-cols-2 items-center text-sm">
					<div class="relative flex h-full items-center pr-2 pl-7">
						<IconGb class="absolute left-0 h-5 w-5" />
						{@render wikiLink('en', animal.englishName, animal.latinName)}
					</div>
					<div
						class="relative flex h-full items-center justify-end border-l border-gray-700/50 pr-7 pl-2 text-right"
					>
						{@render wikiLink('pl', animal.polishName, animal.latinName)}
						<IconPl class="absolute right-0 h-5 w-5" />
					</div>
				</h2>
				<Collapsible.Root>
					<div class="relative flex h-12 items-start justify-center">
						{#if animal.audioSrc}
							<AudioPlayer src={animal.audioSrc} />
						{/if}
						<span class="mx-14 w-full text-center text-xs uppercase italic">{animal.latinName}</span
						>
						<Collapsible.Trigger
							class="group absolute right-0 flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-700/40 p-0.5 text-gray-700 hover:bg-gray-700/30 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-700/60 md:min-h-8 md:min-w-8 print:hidden"
						>
							<IconCaretDown class="h-5 w-5 group-data-[state=open]:hidden" />
							<IconCaretUp class="h-5 w-5 group-data-[state=closed]:hidden" />
						</Collapsible.Trigger>
					</div>
					<Collapsible.Content transition={slide} class="pt-2">
						<Taxonomy classification={animal.classification as Record<string, string>} />
					</Collapsible.Content>
				</Collapsible.Root>
			</div>
		{/each}
	</div>
</div>
