import requests
from bs4 import BeautifulSoup
import re

MAX_DESCRIPTION_LENGTH = 500


def get_description(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    first_paragraph_sentences = (
        re.sub(
            r"\[\d+\]",
            "",
            soup.find("div", class_="mw-content-ltr")
            .findChild("p", class_=lambda x: x != "mw-empty-elt", recursive=False)
            .text,
        )
        .strip()
        .split(".")
    )

    description = ""
    while (
        len(description) < MAX_DESCRIPTION_LENGTH
        and first_paragraph_sentences
        and first_paragraph_sentences[0]
    ):
        description += first_paragraph_sentences.pop(0) + "."
    return description


def get_taxonomy(taxon):
    english_name, english_link = taxon["name"], taxon["link"]
    english_soup = BeautifulSoup(requests.get(english_link).content, "html.parser")

    polish_link = (
        english_soup.find("a", {"lang": "pl"})["href"]
        if english_soup.find("a", {"lang": "pl"})
        else None
    )
    polish_soup = BeautifulSoup(
        requests.get(polish_link).content,
        "html.parser",
    )

    return {
        "english_name": english_name,
        "english_link": english_link,
        "polish_name": re.sub(r"\(.*\)", "", polish_soup.find("h1").text).strip(),
        "polish_link": polish_link,
        "english_description": get_description(english_link),
        "polish_description": get_description(polish_link),
    }
