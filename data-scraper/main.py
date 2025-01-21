import requests
from bs4 import BeautifulSoup
import json

def scrape_birds():
    url = 'https://en.wikipedia.org/wiki/List_of_birds_of_Great_Britain'
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    birds = []
    
    for table in tables:
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 3:
                # Process first cell
                first_cell = cells[0]
                
                # Extract common name and link
                a_tag = first_cell.find('a')
                common_name = ''
                link = ''
                
                if a_tag:
                    common_name = a_tag.get_text(strip=True)
                    link = a_tag.get('href', '')
                
                # Extract remaining text for Latin name
                remaining_text = first_cell.get_text(strip=True)
                latin_name = ''
                
                if '(' in remaining_text and ')' in remaining_text:
                    latin_part = remaining_text.split('(', 1)[1].split(')', 1)[0]
                    latin_name = latin_part.strip()
                
                # Handle cases without links
                if not a_tag:
                    if '(' in remaining_text:
                        common_name = remaining_text.split('(', 1)[0].strip()
                    else:
                        common_name = remaining_text.strip()
                
                # Clean up common name from link text
                if a_tag and common_name in remaining_text:
                    remaining_text = remaining_text.replace(common_name, '').strip()
                
                # Process status
                status_cell = cells[2]
                for sup in status_cell.find_all('sup'):
                    sup.decompose()
                status = status_cell.get_text(' ', strip=True)
                
                # Build full Wikipedia URL
                full_link = f'https://en.wikipedia.org{link}' if link else ''
                
                birds.append({
                    'commonName': common_name,
                    'latinName': latin_name,
                    'link': full_link,
                    'status': status
                })
    
    return birds

def main():
    birds = scrape_birds()
    print(json.dumps(birds, indent=2))

if __name__ == "__main__":
    main()