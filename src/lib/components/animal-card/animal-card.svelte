<script lang="ts">
	import type { Animal } from '$lib/types';

	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';
	import IconCaretDown from '~icons/ion/caret-down';
	import IconCaretUp from '~icons/ion/caret-up';

	import AudioPlayer from '$lib/components/animal-card/animal-card-audio-player.svelte';
	import Taxonomy from '$lib/components/animal-card/animal-card-taxonomy.svelte';
	import { Collapsible } from 'bits-ui';
	import { slide } from 'svelte/transition';

	// Props
	interface Props {
		animal: Animal;
	}

	const { animal }: Props = $props();
</script>

{#snippet wikiLink(text: string, href: string)}
	<a
		class="text-gray-700 underline hover:scale-105 focus-visible:rounded-full focus-visible:outline-4 focus-visible:outline-offset-3 focus-visible:outline-gray-400 active:scale-95"
		{href}
		target="_blank"
		rel="noopener"
	>
		{text}
	</a>
{/snippet}

<div class="flex w-full max-w-lg flex-col gap-2 rounded-3xl bg-gray-50 p-4">
	<img src={animal.imageSrc} alt={animal.latinName} class="rounded-2xl" />
	<h2 class="grid grid-cols-2 items-center text-sm">
		<div class="relative flex h-full items-center pr-2 pl-7">
			<IconGb class="absolute left-0 h-5 w-5" />
			{@render wikiLink(animal.englishName, animal.englishLink)}
		</div>
		<div
			class="relative flex h-full items-center justify-end border-l border-gray-700/50 pr-7 pl-2 text-right"
		>
			{@render wikiLink(animal.polishName, animal.polishLink)}
			<IconPl class="absolute right-0 h-5 w-5" />
		</div>
	</h2>
	<Collapsible.Root>
		<div class="relative flex h-12 items-start justify-center">
			{#if animal.audioSrc}
				<AudioPlayer src={animal.audioSrc} />
			{/if}
			<span class="mx-14 w-full text-center text-xs uppercase italic">{animal.latinName}</span>
			<Collapsible.Trigger
				class="group absolute right-0 flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
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
