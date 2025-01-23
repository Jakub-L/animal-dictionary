import requests
from bs4 import BeautifulSoup
import re

from birds import get_british_bird_links, get_polish_bird_links
from mammals import get_british_mammal_links, get_polish_mammal_links

from infobox import read_british_animal


def main():
    a = list(get_british_bird_links().values())[0]
    # print(get_polish_bird_links())
    b = list(get_british_mammal_links().values())[0]
    # print(get_polish_mammal_links())
    read_british_animal(a)


if __name__ == "__main__":
    main()
