<script lang="ts">
	import { plTaxonomicRanks } from '$lib/data';

	// Props
	interface Props {
		classification: Record<string, string>;
	}

	const { classification }: Props = $props();
</script>

<div class="flex flex-wrap gap-2">
	{#each Object.entries(classification) as [taxon, value]}
		<div class="flex w-full flex-col rounded-full bg-gray-950/20 px-3 py-1">
			<div class="text-2xs flex justify-between font-semibold capitalize">
				<span>{taxon}</span>
				<span>{plTaxonomicRanks[taxon]}</span>
			</div>
			<div class="flex justify-between text-sm capitalize">
				<span>{value}</span>
				<span>{value}</span>
			</div>
		</div>
	{/each}
</div>
