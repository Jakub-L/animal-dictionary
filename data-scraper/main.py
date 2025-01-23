import requests
from bs4 import BeautifulSoup
import re
import json

from birds import get_british_bird_links, get_polish_bird_links
from mammals import get_british_mammal_links, get_polish_mammal_links

from infobox import read_british_animal, read_polish_animal


def main():
    a = list(get_british_bird_links().values())
    b = list(get_british_mammal_links().values())
    c = list(get_polish_bird_links().values())[0]
    d = list(get_polish_mammal_links().values())[0]

    # print(read_british_animal("https://en.wikipedia.org/wiki/Eurasian_lynx"))

    for url in a + b:
        try:
            animal = read_british_animal(url)
            with open("animals.json", "a") as f:
                f.write(json.dumps(animal) + "\n")
        except:
            print(url)


if __name__ == "__main__":
    main()
