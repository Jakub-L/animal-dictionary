from bs4 import BeautifulSoup
import requests
import re

BRITISH_MAMMALS_URL = "https://en.wikipedia.org/wiki/List_of_mammals_of_Great_Britain"
POLISH_MAMMALS_URL = "https://pl.wikipedia.org/wiki/Ssaki_Polski"


def get_british_mammal_links():
    """
    Scrapes a webpage containing a list of British mammals and extracts their Wikipedia links.

    This function sends a GET request to the URL specified by the global variable `BRITISH_MAMMALS_URL`,
    parses the HTML content using BeautifulSoup, and searches for list items (`<li>`) that contain
    mammal names and their corresponding Wikipedia links. It filters out items that do not contain
    an italic tag (`<i>`, the Latin name) or have the text "EX" (indicating extinct species). The
    function then constructs a dictionary where the keys are the lowercase names of the mammals and
    the values are the full URLs to their Wikipedia pages.

    Returns:
      dict: A dictionary where the keys are mammal names (in lowercase) and the values are the
          corresponding Wikipedia URLs.
    """
    soup = BeautifulSoup(requests.get(BRITISH_MAMMALS_URL).content, "html.parser")
    links = {}
    for li in soup.find_all("li"):

        i_tag = li.find("i")
        if not i_tag or "EX" in li.get_text():
            continue
        a_tag = li.find("a")
        if a_tag and a_tag.get("href").startswith("/wiki/"):
            name = a_tag["title"].lower()
            link = f"http://en.wikipedia.org{a_tag['href'].lower()}"
            links[name] = link
    return links


def get_polish_mammal_links():
    """
    Fetches and parses a list of Polish mammal links from a specified Wikipedia page.

    This function sends a GET request to the URL defined by POLISH_MAMMALS_URL, parses the HTML content
    to find tables with the class "wikitable", and extracts mammal names and their corresponding Wikipedia
    links. The function returns a dictionary where the keys are the mammal names (in lowercase and with
    bracketed text removed) and the values are the full URLs to their respective Wikipedia pages.

    Returns:
      dict: A dictionary with mammal names as keys and their corresponding Wikipedia links as values.
    """
    soup = BeautifulSoup(requests.get(POLISH_MAMMALS_URL).content, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    links = {}
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) > 1:
                try:
                    # Check if the table has 5 columns (Full row) or not (row with rowspanning cells)
                    raw_name = cells[2 if len(cells) == 5 else 0].get_text().lower()
                    raw_link = (
                        cells[2 if len(cells) == 5 else 0].find("a")["href"]
                    )
                except:
                    continue

                # Strip bracketed text (Latin name on British page)
                name = re.sub(r"\(.*\)|†", r"", raw_name)
                link = f"http://pl.wikipedia.org{raw_link}"

                links[name] = link
    return links
