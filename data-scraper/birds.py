from bs4 import BeautifulSoup
import requests
import re

# Types
type BirdConfig = dict[str, str | function]

# URLs
BRITISH_BIRDS_URL = "https://en.wikipedia.org/wiki/List_of_birds_of_Great_Britain"
POLISH_BIRDS_URL = "https://pl.wikipedia.org/wiki/Ptaki_Polski"


# Utils
def is_british_bird_status_valid(cells: list[str]) -> bool:
    try:
        [category, status] = cells[2].get_text().split(" – ")
        return category == "A" and not any(
            element in status for element in ["rare", "scarce", "vagrant"]
        )
    except ValueError:
        return False


def is_polish_bird_status_valid(cells: list[str]) -> bool:
    category = cells[2].get_text()
    status = cells[3].get_text()
    return category == "A" and not any(
        element in status for element in ["zalatuje", "skrajnie nielicznie"]
    )


def read_bird_table(soup: BeautifulSoup, config: BirdConfig) -> dict[str, str]:
    tables = soup.find_all("table", {"class": "wikitable"})
    links = {}
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) > 1:
                try:
                    raw_name = cells[config["name_column"]].get_text().lower()
                    raw_link = cells[config["name_column"]].find("a")["href"].lower()
                except:
                    continue

                # Strip bracketed text (Latin name on British page)
                name = re.sub(r"\(.*\)", r"", raw_name)
                link = f"http://{config["lang"]}.wikipedia.org{raw_link}"

                if config["status_function"](cells) and not "redlink=1" in link:
                    links[name] = link
    return links


# Configs
british_bird_table_config: BirdConfig = {
    "lang": "en",
    "name_column": 0,
    "status_function": is_british_bird_status_valid,
}

polish_bird_table_config: BirdConfig = {
    "lang": "pl",
    "name_column": 0,
    "status_function": is_polish_bird_status_valid,
}


# Main
def get_british_bird_links() -> dict[str, str]:
    soup = BeautifulSoup(requests.get(BRITISH_BIRDS_URL).content, "html.parser")
    return read_bird_table(soup, british_bird_table_config)


def get_polish_bird_links() -> dict[str, str]:
    soup = BeautifulSoup(requests.get(POLISH_BIRDS_URL).content, "html.parser")
    return read_bird_table(soup, polish_bird_table_config)
