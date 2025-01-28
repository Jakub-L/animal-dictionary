<script lang="ts">
	import '../app.css';
	import { data } from '$lib/data';

	console.log(data);
</script>

<div class="flex flex-col gap-4 p-4">
{#each data as animal}
	<div class="border border-slate-950 rounded-3xl p-4 flex flex-col gap-2">
		<img src={animal.imageSrc} alt={animal.latinName} class="rounded-2xl"/>
		<h2 class="grid grid-cols-2">
			<span>{animal.englishName}</span>
			<span class="text-right border-l border-slate-950">{animal.polishName}</span>
		</h2>
	</div>
{/each}
</div>