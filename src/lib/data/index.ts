import birds from './birds.json';
import mammals from './mammals.json';
import reptiles from './reptiles.json';

export const plTaxonomicRanks: Record<string, string> = {
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

export const animals = [...birds, ...mammals, ...reptiles];
