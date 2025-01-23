import requests
from bs4 import BeautifulSoup
import re


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
        cells = rows[i].find_all("td")
        key = cells[0].get_text().strip().lower().replace(":", "")
        value = cells[1].get_text().strip().lower()
        if key == "species":
            return classification
        classification[key] = value
    return classification


def read_british_animal(url):
    """
    Extracts information about a British animal from a given Wikipedia URL.

    Args:
        url (str): The URL of the Wikipedia page containing the animal's information.

    Returns:
        None: This function prints the extracted animal information.

    The extracted information includes:
        - english_name (str): The English name of the animal.
        - img_file (str): The URL of the animal's image.
        - latin_name (str, optional): The Latin (binomial) name of the animal.
        - classification (dict, optional): The scientific classification of the animal.
        - audio (str, optional): The URL of the animal's audio file.
    """
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
    print(animal)
