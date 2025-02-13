<script lang="ts">
	import { Dialog } from 'bits-ui';

	import IconInfo from '~icons/ion/information-circle-outline';
	import IconClose from '~icons/ion/close';
	import type { Taxon } from '$lib/types';

	// Props
	interface Props {
		taxon: Taxon;
	}

	const { taxon }: Props = $props();
</script>

<Dialog.Root>
	<Dialog.Trigger
		disabled={!taxon}
		class="flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500 disabled:opacity-50 disabled:hover:bg-transparent"
	>
		<IconInfo class="h-6 w-6" />
	</Dialog.Trigger>
	<Dialog.Portal>
		<Dialog.Overlay class="fixed inset-0 z-50 bg-gray-950/50" />
		<Dialog.Content
			class="fixed top-[50%] left-[50%] z-50 w-full max-w-md translate-x-[-50%] translate-y-[-50%] rounded-lg bg-gray-50 p-4 "
		>
			<div class="flex items-center justify-between">
				<Dialog.Title class="flex font-semibold capitalize">
					<span class="pr-4">{taxon.englishName}</span>
					<span class="border-l border-gray-700/50 pl-4">{taxon.polishName}</span>
				</Dialog.Title>
				<Dialog.Close
					class="flex min-h-12 min-w-12 items-center justify-center rounded-full p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
				>
					<IconClose class="h-8 w-8" />
				</Dialog.Close>
			</div>
			<Dialog.Description class="flex flex-col gap-4 text-sm leading-relaxed">
				<p class="border-b border-gray-700/50 pb-4">{taxon.englishDescription}</p>
				<div class="flex justify-between">
					<a
						class="text-gray-700 underline hover:scale-105 focus-visible:rounded-full focus-visible:outline-4 focus-visible:outline-offset-3 focus-visible:outline-gray-400 active:scale-95"
						href={taxon.englishLink}
						target="_blank"
						rel="noopener"
					>
						Read more...
					</a>
					<a
						class="text-gray-700 underline hover:scale-105 focus-visible:rounded-full focus-visible:outline-4 focus-visible:outline-offset-3 focus-visible:outline-gray-400 active:scale-95"
						href={taxon.polishLink}
						target="_blank"
						rel="noopener"
					>
						Czytaj więcej...
					</a>
				</div>
			</Dialog.Description>
		</Dialog.Content>
	</Dialog.Portal>
</Dialog.Root>
