<script lang="ts">
	import '../app.css';

	import IconPl from '~icons/circle-flags/pl';
	import IconGb from '~icons/circle-flags/gb';

	import { data } from '$lib/data';
</script>

<div class="flex flex-col gap-4 p-4">
	{#each data as animal}
		<div class="flex flex-col gap-2 rounded-3xl bg-gray-50 p-4">
			<img src={animal.imageSrc} alt={animal.latinName} class="rounded-2xl" />
			<div class="grid grid-cols-2 items-center">
				<div class="relative flex h-full items-center pr-2 pl-7">
					<IconGb class="absolute left-0 h-5 w-5" />
					<h2>{animal.englishName}</h2>
				</div>
				<div
					class="relative flex h-full items-center border-l border-gray-950 pr-7 pl-2 text-right"
				>
					<h2>{animal.polishName}</h2>
					<IconPl class="absolute right-0 h-5 w-5" />
				</div>
			</div>
		</div>
	{/each}
</div>
