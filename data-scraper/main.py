import requests
import json
from pathlib import Path

from birds import get_british_bird_links, get_polish_bird_links
from mammals import get_british_mammal_links, get_polish_mammal_links
from infobox import read_animal


def kebab_case(string):
    return string.lower().replace(" ", "-")


def get_file(url, base_path):
    headers = {"User-Agent": "Mozilla/5.0"}
    extension = Path(url).suffix
    response = requests.get(url, headers=headers)
    with open(f"{base_path}{extension}", "wb") as file:
        file.write(response.content)


def main():
    urls = (
        get_british_bird_links()
        + get_british_mammal_links()
        + get_polish_bird_links()
        + get_polish_mammal_links()
    )

    Path("../static").mkdir(exist_ok=True)
    Path("../static/audio").mkdir(exist_ok=True)
    Path("../static/images").mkdir(exist_ok=True)

    with open("data.json", "w") as file:
        file.write("[\n")
        for url in urls:
            try:
                animal = read_animal(url)
                raw_json = {
                    "englishName": animal["english_name"],
                    "polishName": animal["polish_name"],
                    "latinName": animal["latin_name"],
                    "classification": animal["classification"],
                }
                file.write(json.dumps(raw_json, indent=4))
                file.write(",\n")
                if "img_file" in animal:
                    get_file(
                        animal["img_file"],
                        f"../static/images/{kebab_case(animal['latin_name'])}",
                    )
                if "audio" in animal:
                    get_file(
                        animal["audio"],
                        f"../static/audio/{kebab_case(animal['latin_name'])}",
                    )
            except Exception as e:
                print(f"Error reading {url}: {e}")
                continue
        file.write("]")


if __name__ == "__main__":
    main()
