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
    """Check if a bird species' British status is valid for a common British bird.

    This function determines if a bird species is commonly found in Britain based on its
    British Ornithologists' Union (BOU) category and status. A bird is considered valid if it:
    - Has Category A status (species recorded in an apparently natural state)
    - Is not classified as rare, scarce, or vagrant

    Args:
        cells (list[str]): List of table cells containing bird information, where cells[2]
            contains the British status in format "Category – Status"

    Returns:
        bool: True if the bird is a common Category A species, False otherwise or if the
            status format is invalid
    """
    try:
        [category, status] = cells[2].get_text().split(" – ")
        return category == "A" and not any(
            element in status for element in ["rare", "scarce", "vagrant"]
        )
    except ValueError:
        return False


def is_polish_bird_status_valid(cells: list[str]) -> bool:
    """Validates if a bird's status in Poland meets specific criteria.

    This function checks if a bird is a regular species (category A) in Poland and is not
    classified as vagrant or extremely rare.

    Args:
        cells (list[str]): List of table cells containing bird information, where:
            - cells[2] contains the bird category
            - cells[3] contains the bird status

    Returns:
        bool: True if the bird is category A and not vagrant/extremely rare, False otherwise
    """
    category = cells[2].get_text()
    status = cells[3].get_text()
    return category == "A" and not any(
        element in status for element in ["zalatuje", "skrajnie nielicznie"]
    )


def read_bird_table(soup: BeautifulSoup, config: BirdConfig) -> dict[str, str]:
    """Extracts bird names and corresponding Wikipedia links from a table on a Wikipedia page.

    This function processes HTML tables with a 'wikitable' class, extracting bird names and their
    corresponding Wikipedia page URLs based on the configuration provided. It filters entries
    based on a status function defined in the configuration.

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing the parsed HTML of the Wikipedia page
        config (BirdConfig): Configuration object containing:
            - name_column: Index of the column containing bird names
            - lang: Wikipedia language domain (e.g., 'en' for English)
            - status_function: Function that determines if a row should be included

    Returns:
        dict[str, str]: Dictionary mapping bird names (lowercase) to their Wikipedia URLs.
                       Only includes entries that pass the status check and have valid links.
    """
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
    """
    Retrieves links to bird species pages from the British birds website.

    Returns
    -------
    dict[str, str]
        Dictionary mapping bird species names to their corresponding URLs on the website.
        Format: {'bird_name': 'url_to_bird_page'}
    """
    soup = BeautifulSoup(requests.get(BRITISH_BIRDS_URL).content, "html.parser")
    return read_bird_table(soup, british_bird_table_config)


def get_polish_bird_links() -> dict[str, str]:
    """
    Retrieves links to bird species pages from the Polish birds website.

    Returns
    -------
    dict[str, str]
        Dictionary mapping bird species names to their corresponding URLs on the website.
        Format: {'bird_name': 'url_to_bird_page'}
    """
    soup = BeautifulSoup(requests.get(POLISH_BIRDS_URL).content, "html.parser")
    return read_bird_table(soup, polish_bird_table_config)
