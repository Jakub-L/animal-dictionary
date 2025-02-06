import type { Animal, TaxonFilter } from '$lib/types';

/**
 * Strips string of all non-alphabetic (including Polish) characters and converts it to lowercase.
 * @param {string} str - String to be stripped.
 * @returns {string} - Stripped string.
 */
const stripString = (str: string): string =>
	str
		.toLowerCase()
		.trim()
		.replace(/[^a-ząęóćńśźżł ]/g, '');

/**
 * Splits string into words (by space) and returns word at given index. The string is also
 * stripped of all non-alphabetic (including Polish) characters and converted to lowercase.
 *
 * @param {string} str - String to be split.
 * @param {number} idx - Index of the word to be returned.
 * @returns {string} - Word at given index, or empty string if index is out of bounds.
 */
const getWordAt = (str: string, idx: number): string => {
	return stripString(str).split(' ').at(idx) ?? '';
};

/**
 * Shuffles an array using the Fisher-Yates algorithm. Returns a
 * shallow copy of the original array.
 *
 * @param {T[]} arr - Array to be shuffled.
 * @returns {T[]} - Shuffled array.
 */
const shuffleArray = <T>(arr: T[]): void => {
	for (let i = arr.length - 1; i >= 1; i--) {
		const j = Math.floor(Math.random() * (i + 1));
		[arr[i], arr[j]] = [arr[j], arr[i]];
	}
};

/**
 * Sorts an array of animals according to the ordering. The animals are sorted by their
 * common name, i.e. "long-tailed tit" will be sorted with the T's not the L's. It is
 * assumed that in English the common name is the last word of the name, and in Polish
 * that it is the first. If any other ordering is supplied, the array will be shuffled.
 *
 * @param {Animal[]} arr - Animal array to sort
 * @param {string} ordering - What ordering to use
 * @returns {Animal[]} The sorted array
 */
const sortAnimals = (arr: Animal[], ordering: string): Animal[] => {
	const newArr = [...arr];
	if (ordering === 'en') {
		newArr.sort((a, b) =>
			getWordAt(a.englishName, -1).localeCompare(getWordAt(b.englishName, -1), 'en')
		);
	} else if (ordering === 'pl') {
		newArr.sort((a, b) =>
			getWordAt(a.polishName, 0).localeCompare(getWordAt(b.polishName, 0), 'pl')
		);
	} else shuffleArray(newArr);
	return newArr;
};

/**
 * Filters an array of animals based on name search and taxonomic classification criteria.
 *
 * @param {Animal[]} arr - Array of Animal objects to filter
 * @param {string} nameQuery - Search string to filter animals by name (English, Latin, or Polish)
 * @param {TaxonFilter} taxonFilter - Object containing taxonomic filters to apply
 * @returns {Animal[]} Filtered array of Animal objects matching both name and taxonomic criteria
 */
const filterAnimals = (arr: Animal[], nameQuery: string, taxonFilter: TaxonFilter): Animal[] => {
	return arr
		.filter((animal) =>
			[animal.englishName, animal.latinName, animal.polishName]
				.map((s) => s.toLowerCase())
				.some((s) => s.includes(nameQuery))
		)
		.filter(({ classification }) => {
			for (const [taxon, value] of Object.entries(classification)) {
				if (
					taxon in taxonFilter &&
					taxonFilter[taxon].length > 0 &&
					!taxonFilter[taxon].includes(value as string)
				)
					return false;
			}
			return true;
		});
};

export { filterAnimals, sortAnimals };
