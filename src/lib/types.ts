export type Animal = {
	englishName: string;
	polishName: string;
	latinName: string;
	classification: Record<string, string | undefined>;
	imageSrc: string | null;
	audioSrc: string | null;
};
