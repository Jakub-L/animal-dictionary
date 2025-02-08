import json

from birds import get_british_bird_links, get_polish_bird_links
from mammals import get_british_mammal_links, get_polish_mammal_links
from infobox import read_animal
from taxonomy import get_taxonomy


def process_group(group, output_name, taxon_links):
    processed_animals = set()
    with open(f"../src/lib/data/{output_name}.json", "w") as file:
        file.write("[\n")
        for url in group:
            try:
                animal = read_animal(url)
                if animal["latin_name"] in processed_animals:
                    continue
                processed_animals.add(animal["latin_name"])

                classification = {}
                for taxon, taxon_data in animal["classification"].items():
                    name = taxon_data["name"]
                    taxon_links[name] = taxon_data
                    classification[taxon] = name

                raw_json = {
                    "englishName": animal["english_name"],
                    "polishName": animal["polish_name"],
                    "latinName": animal["latin_name"],
                    "englishLink": animal["english_link"],
                    "polishLink": animal["polish_link"],
                    "classification": classification,
                    "imageSrc": animal["img_file"] if "img_file" in animal else None,
                    "audioSrc": animal["audio"] if "audio" in animal else None,
                }
                file.write(json.dumps(raw_json, indent=4))
                file.write(",\n")
            except Exception as e:
                print(f"Error reading {url}: {e}")
                continue
        file.write("]")


def process_taxonomy(taxon_links):
    processed_taxons = set()
    with open(f"../src/lib/data/taxonomy.json", "w") as file:
        file.write("[\n")
        for taxon_name, taxon in taxon_links.items():
            try:
                if taxon_name in processed_taxons:
                    continue
                processed_taxons.add(taxon_name)
                taxon_data = get_taxonomy(taxon)
                raw_json = {
                    "englishName": taxon_data["english_name"],
                    "polishName": taxon_data["polish_name"],
                    "englishLink": taxon_data["english_link"],
                    "polishLink": taxon_data["polish_link"],
                    "englishDescription": taxon_data["english_description"],
                    "polishDescription": taxon_data["polish_description"],
                }
                file.write(json.dumps(raw_json, indent=4))
                file.write(",\n")
            except Exception as e:
                print(f"Error saving taxon {taxon_name}: {e}")
                continue
        file.write("]")


def read_manual_imports():
    groups = {}
    with open("./manual.json", "r") as file:
        data = json.load(file)
        for animal in data:
            if animal["output"] not in groups:
                groups[animal["output"]] = []
            groups[animal["output"]].append(animal["url"])
    return groups


def main():
    groups = {
        "birds": get_polish_bird_links()[0:] + get_british_bird_links(),
        "mammals": get_polish_mammal_links() + get_british_mammal_links(),
    }
    taxon_links = {}

    for group_name, group in read_manual_imports().items():
        groups.setdefault(group_name, []).extend(group)

    for group_name, group in groups.items():
        process_group(group, group_name, taxon_links)

    process_taxonomy(taxon_links)


if __name__ == "__main__":
    main()
