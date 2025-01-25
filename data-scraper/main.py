import json
from pathlib import Path

from birds import get_british_bird_links, get_polish_bird_links
from mammals import get_british_mammal_links, get_polish_mammal_links
from infobox import read_animal


def process_group(group, output_name):
    processed_animals = set()
    with open(f"../static/data/{output_name}.json", "w") as file:
        file.write("[\n")
        for url in group:
            try:
                animal = read_animal(url)
                if animal["latin_name"] in processed_animals:
                    continue
                processed_animals.add(animal["latin_name"])
                raw_json = {
                    "englishName": animal["english_name"],
                    "polishName": animal["polish_name"],
                    "latinName": animal["latin_name"],
                    "classification": animal["classification"],
                    "imageSrc": animal["img_file"] if "img_file" in animal else None,
                    "audioSrc": animal["audio"] if "audio" in animal else None,
                }
                file.write(json.dumps(raw_json, indent=4))
                file.write(",\n")
            except Exception as e:
                print(f"Error reading {url}: {e}")
                continue
        file.write("]")


def main():
    birds = get_polish_bird_links() + get_british_bird_links()
    mammals = get_polish_mammal_links() + get_british_mammal_links()
    process_group(birds, "birds")
    process_group(mammals, "mammals")


if __name__ == "__main__":
    main()
