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
    image_container = soup.find("div", {"class": "fullImageLink"})

    return f"https:{image_container.find("img")["src"]}" if image_container else None


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


def get_classification(rows, start_index, domain):
    """
    Extracts classification information from a list of HTML table rows.

    Args:
        rows (list): A list of BeautifulSoup Tag objects representing table rows.
        start_index (int): The index to start extracting classification information from.
        domain (str): The domain of the webpage to scrape.

    Returns:
        dict: A dictionary containing classification information where keys are classification
              categories (e.g., 'kingdom', 'phylum', etc.) and values are the corresponding
              classification names and links. The extraction stops when the 'species' key is encountered.
    """
    classification = {}
    for i in range(start_index, len(rows)):
        cells = rows[i].find_all(["td", "th"])
        key = cells[0].get_text().strip().lower().replace(":", "")
        name = list(cells[1].stripped_strings)[0].lower()
        a_tag = cells[1].find("a")
        link = a_tag["href"] if a_tag and a_tag.has_attr("href") else None
        if key == "species complex":
            continue
        if key == "species" or key == "gatunek":
            return classification
        classification[key] = {
            "name": name,
            "link": f"{domain}{link}" if link else None,
        }
    return classification


def merge_animals(english, polish):
    english["polish_name"] = polish["polish_name"]
    english["img_file"] = english["img_file"] or polish["img_file"]
    english["polish_link"] = polish["polish_link"]
    return english


def read_british_animal(url, ignore_other_language=False):
    domain = url.split("/wiki/")[0]
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rows = soup.find("table", {"class": "infobox"}).find_all("tr")
    animal = {
        "english_name": re.sub(r"\[.*\]|\n.*", r"", list(rows[0].stripped_strings)[0]),
        "img_file": get_image(f"{domain}{rows[1].find("a")["href"]}"),
        "english_link": url,
    }
    for i, row in enumerate(rows):
        if row.get_text().strip() == "Binomial name":
            animal["latin_name"] = re.sub(
                r"\(.*\)|,.*", r"", list(rows[i + 1].stripped_strings)[0].lower()
            )
        if row.get_text().strip() == "Scientific classification":
            animal["classification"] = get_classification(rows, i + 1, domain)

        audio = row.find("audio")
        if audio is not None:
            source = audio.find("source")
            resource = audio["resource"] if "resource" in audio else None
            audio_url = resource if resource else source["src"]
            if source:
                animal["audio"] = f"https:{audio_url}"
            else:
                animal["audio"] = get_audio(f"{domain}{audio_url}")

    polish_link = soup.find("a", {"lang": "pl"})
    polish_animal = {}
    if not ignore_other_language:
        if polish_link:
            polish_animal = read_polish_animal(polish_link["href"], True)
        else:
            return None
    return merge_animals(animal, polish_animal) if not ignore_other_language else animal


def read_polish_animal(url, ignore_other_language=False):
    domain = url.split("/wiki/")[0]
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rows = soup.find("table", {"class": "infobox"}).find_all("tr")
    animal = {
        "polish_name": soup.find("table", {"class": "infobox"})
        .find("caption")
        .get_text()
        .strip(),
        "latin_name": re.sub(r"\[.*\]", r"", list(rows[0].stripped_strings)[0].lower()),
        "img_file": get_image(f"{domain}{rows[3].find("a")["href"]}"),
        "polish_link": url,
    }
    english_link = soup.find("a", {"lang": "en"})["href"]
    english_animal = {}
    if not ignore_other_language:
        if english_link:
            english_animal = read_british_animal(english_link, True)
        else:
            return None
    return (
        merge_animals(english_animal, animal) if not ignore_other_language else animal
    )


def read_animal(url):
    prefix = re.split(r"//|\.", url)[1]
    return read_british_animal(url) if prefix == "en" else read_polish_animal(url)
