from bs4 import BeautifulSoup
import requests
import re

BRITISH_MAMMALS_URL = "https://en.wikipedia.org/wiki/List_of_mammals_of_Great_Britain"
POLISH_MAMMALS_URL = "https://pl.wikipedia.org/wiki/Ssaki_Polski"


def get_british_mammal_links():
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
    soup = BeautifulSoup(requests.get(POLISH_MAMMALS_URL).content, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    links = {}
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) > 1:
                try:
                    raw_name = cells[2 if len(cells) == 5 else 0].get_text().lower()
                    raw_link = (
                        cells[2 if len(cells) == 5 else 0].find("a")["href"].lower()
                    )
                except:
                    continue

                # Strip bracketed text (Latin name on British page)
                name = re.sub(r"\(.*\)|†", r"", raw_name)
                link = f"http://pl.wikipedia.org{raw_link}"

                links[name] = link
    return links
