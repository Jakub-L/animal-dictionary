import type { Animal } from '$lib/types';

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
const shuffleArray = <T>(arr: T[]): T[] => {
	const newArr = [...arr];
	for (let i = newArr.length - 1; i >= 1; i--) {
		const j = Math.floor(Math.random() * (i + 1));
		[newArr[i], newArr[j]] = [newArr[j], newArr[i]];
	}
	return newArr;
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
	if (ordering === 'en') {
		return arr.toSorted((a, b) =>
			getWordAt(a.englishName, -1).localeCompare(getWordAt(b.englishName, -1), 'en')
		);
	} else if (ordering === 'pl') {
		return arr.toSorted((a, b) =>
			getWordAt(a.polishName, 0).localeCompare(getWordAt(b.polishName, 0), 'pl')
		);
	}
	return shuffleArray(arr);
};

export { sortAnimals };
