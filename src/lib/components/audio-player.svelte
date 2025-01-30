<script lang="ts">
	import IconPlay from '~icons/ion/play';
	import IconStop from '~icons/ion/stop';

	// Props
	interface Props {
		src: string;
	}

	const { src }: Props = $props();

	// State
	let isPlaying: boolean = $state(false);
	let audioPlayer: HTMLAudioElement;

	// Handlers
	const toggleAudio = () => {
		if (isPlaying) {
			audioPlayer.pause();
			audioPlayer.currentTime = 0;
		} else {
			audioPlayer.play();
		}
		isPlaying = !isPlaying;
	};
</script>

<div>
	<button
		class="absolute flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-700/40 p-0.5 text-gray-700 hover:bg-gray-700/30 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-700/60 md:min-h-8 md:min-w-8 print:hidden"
		aria-label={isPlaying ? 'Stop audio' : 'Play audio'}
		onclick={toggleAudio}
	>
		{#if isPlaying}
			<IconStop class="h-5 w-5" />
		{:else}
			<IconPlay class="h-5 w-5" />
		{/if}
	</button>
	<audio bind:this={audioPlayer} {src} {ontimeupdate}></audio>
</div>
