import birds from './birds.json';
import mammals from './mammals.json';
import reptiles from './reptiles.json';

import taxonTranslations from './taxons.json';

import type { Animal } from '$lib/types';
import { sortAnimals } from '$lib/utils';

export const taxons: Record<string, string> = taxonTranslations;
export const taxonomicRanks: Record<string, string> = {
	domain: 'domena',
	kingdom: 'królestwo',
	phylum: 'typ',
	class: 'gromada',
	order: 'rząd',
	family: 'rodzina',
	genus: 'rodzaj',
	subgenus: 'podrodzaj',
	clade: 'klad',
	subfamily: 'podrodzina',
	tribe: 'plemię',
	suborder: 'podrząd',
	infraorder: 'infrarząd',
	infraclass: 'infragromada',
	'species complex': 'kompleks gatunków'
};

export const animals: Animal[] = $state([...birds, ...mammals, ...reptiles]);
export const filteredAnimals: { value: Animal[] } = $state({ value: sortAnimals(animals, 'en') });
