import requests
from bs4 import BeautifulSoup
import re
from birds import get_british_bird_links, get_polish_bird_links
from mammals import get_british_mammal_links, get_polish_mammal_links


def main():
    # print(get_british_bird_links())
    # print(get_polish_bird_links())
    print(get_british_mammal_links())
    # print(get_polish_mammal_links())


if __name__ == "__main__":
    main()
