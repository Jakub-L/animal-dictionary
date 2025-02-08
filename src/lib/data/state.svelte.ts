import amphibians from './amphibians.json';
import birds from './birds.json';
import mammals from './mammals.json';
import reptiles from './reptiles.json';

import taxonomy from './taxonomy.json';

import type { Animal, Taxon, TaxonFilter } from '$lib/types';

export const taxons: Record<string, Taxon> = taxonomy.reduce(
	(acc, taxon) => ({ ...acc, [taxon.englishName]: taxon }),
	{}
);
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
	infraclass: 'infragromada'
};

export const animals: Animal[] = [...amphibians, ...birds, ...mammals, ...reptiles];

export const nameQuery: { value: string } = $state({ value: '' });
export const taxonFilters: { value: TaxonFilter } = $state({ value: {} });

export const ordering: { value: string } = $state({ value: 'en' });
