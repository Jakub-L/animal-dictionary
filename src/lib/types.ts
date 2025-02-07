export type Animal = {
	englishName: string;
	polishName: string;
	latinName: string;
	englishLink: string;
	polishLink: string;
	classification: Record<string, string | undefined>;
	imageSrc: string | null;
	audioSrc: string | null;
};

export type TaxonFilter = Record<string, string>;
