<script lang="ts">
	import { Dialog } from 'bits-ui';

	import IconInfo from '~icons/ion/information-circle-outline';
	import IconClose from '~icons/ion/close';
</script>

<Dialog.Root>
	<Dialog.Trigger
		class="flex min-h-12 min-w-12 items-center justify-center rounded-full border border-gray-400 p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
	>
		<IconInfo class="h-6 w-6" />
	</Dialog.Trigger>
	<Dialog.Portal>
		<Dialog.Overlay class="fixed inset-0 bg-gray-950/50 z-50"/>
		<Dialog.Content class="fixed left-[50%] top-[50%] z-50 w-full max-w-md translate-x-[-50%] -translate-y-[-50%] bg-gray-50 p-4 rounded-lg">
			<div class="flex justify-between items-center">
				<Dialog.Title class="font-semibold">Info</Dialog.Title>
				<Dialog.Close
					class="flex min-h-12 min-w-12 items-center justify-center rounded-full p-0.5 text-gray-700 hover:bg-gray-400 focus-visible:outline-4 focus-visible:-outline-offset-1 focus-visible:outline-gray-400 active:bg-gray-500"
				>
					<IconClose class="h-8 w-8" />
				</Dialog.Close>
			</div>
			<Dialog.Description>Hello</Dialog.Description>
		</Dialog.Content>
	</Dialog.Portal>
</Dialog.Root>
