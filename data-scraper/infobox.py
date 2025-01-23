import requests
from bs4 import BeautifulSoup
import re

TAXONOMY_PAIRS = {
    "domain": "domena",
    "kingdom": "królestwo",
    "phylum": "typ",
    "class": "gromada",
    "infraclass": "infragromada",
    "clade": "klad",
    "order": "rząd",
    "infraorder": "infrarząd",
    "suborder": "podrząd",
    "tribe": "plemię",
    "family": "rodzina",
    "subfamily": "podrodzina",
    "genus": "rodzaj",
    "subgenus": "podrodzaj",
}


def get_image(url):
    """
    Fetches the image URL from a given webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The full URL of the image found on the webpage.
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    img = soup.find("div", {"class": "fullImageLink"}).find("img")["src"]
    return f"https:{img}"


def get_audio(url):
    """
    Extracts the audio file URL from a given webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The full URL of the audio file.
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    audio = soup.find("div", {"class": "fullMedia"}).find("a")["href"]
    return f"https:{audio}"


def get_classification(rows, start_index):
    """
    Extracts classification information from a list of HTML table rows.

    Args:
        rows (list): A list of BeautifulSoup Tag objects representing table rows.
        start_index (int): The index to start extracting classification information from.

    Returns:
        dict: A dictionary containing classification information where keys are classification
              categories (e.g., 'kingdom', 'phylum', etc.) and values are the corresponding
              classification names. The extraction stops when the 'species' key is encountered.
    """
    classification = {}
    for i in range(start_index, len(rows)):
        cells = rows[i].find_all(["td", "th"])
        key = cells[0].get_text().strip().lower().replace(":", "")
        value = cells[1].get_text().strip().lower()
        if key == "species" or key == "gatunek":
            return classification
        classification[key] = value
    return classification


def merge_animals(english, polish):
    english["polish_name"] = polish["polish_name"]


def read_british_animal(url, ignore_other_language=False):
    domain = url.split("/wiki/")[0]
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rows = soup.find("table", {"class": "infobox"}).find_all("tr")
    animal = {
        "english_name": re.sub(r"\[.*\]", r"", rows[0].get_text().strip()),
        "img_file": get_image(f"{domain}{rows[1].find("a")["href"]}"),
    }
    for i, row in enumerate(rows):
        if row.get_text().strip() == "Binomial name":
            animal["latin_name"] = re.sub(
                r"\(.*\)", r"", rows[i + 1].get_text().strip().lower()
            )
        if row.get_text().strip() == "Scientific classification":
            animal["classification"] = get_classification(rows, i + 1)
        if row.find("audio") is not None:
            animal["audio"] = get_audio(f"{domain}{row.find("audio")["resource"]}")

    polish_link = soup.find("a", {"lang": "pl"})["href"]
    if not ignore_other_language and polish_link:
        polish_animal = read_polish_animal(polish_link, True)

    return animal


def read_polish_animal(url, ignore_other_language=False):
    domain = url.split("/wiki/")[0]
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rows = soup.find("table", {"class": "infobox"}).find_all("tr")
    animal = {
        "polish_name": soup.find("table", {"class": "infobox"})
        .find("caption")
        .get_text()
        .strip()
        .lower(),
        "latin_name": re.sub(r"\[.*\]", r"", rows[0].get_text().strip().lower()),
        "img_file": get_image(f"{domain}{rows[3].find("a")["href"]}"),
    }
    for i, row in enumerate(rows):
        if row.get_text().strip() == "Systematyka":
            animal["classification"] = get_classification(rows, i + 1)

    english_link = soup.find("a", {"lang": "en"})["href"]
    if not ignore_other_language and english_link:
        english_animal = read_british_animal(english_link, True)
        print(english_animal)

    return animal
