"""Program represents a microservice to a video game companion tool.
The microservice provides data related to in-game items and item 
attributes by scraping a community wiki page."""
import urllib.request
from bs4 import BeautifulSoup
import json

def main() -> None:
    """
    Checks for request, scrapes html from wiki page, 
    and responds with the file name with item data
    """
    # Check for request
    while True:
        with open("pipe.txt", "r") as infile:
            line = infile.read()
        
        if line == "Get Weapon Data":
            print("Received Request")
            # Get data
            items = scrape_weapons()
        
            print("Posting data")
            with open("weapon_data.json", 'w') as outfile:
                json.dump(items, outfile, indent=4)

            print('Sending Response')
            with open("pipe.txt", "w") as file:
                file.write("weapon_data.json")
            print('Response Sent')

def scrape_weapons():
    """Retrieves information from wiki page using
    beautiful soup library.
    https://beautiful-soup-4.readthedocs.io/en/latest/
    """
    # Open URL, read HTML, and scrape tags 
    url = 'http://dnd5e.wikidot.com/weapons/'
    html_page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    # Store Weapon Data in dictionary
    weapon_dict = dict()
    attrib_list = ["Cost", "Damage", "Weight", "Properties"]
    attrib_info = [""] * 4

    # Iterate through html tags and store relevant info
    start, end, idx = False, False, 0
    for tag in soup.find_all(['h1', 'th', 'td']):
        if str(tag.get_text()) == "Simple Weapons":
            start = True
        if str(tag.get_text()) == "Ammunition":
            end = True

        # Item Types   
        if start and not end:
            if str(tag.name) == 'h1':
                heading = str(tag.get_text())
                weapon_dict[heading] = dict()

            # Items and attributes
            if str(tag.name) == 'td':
                if idx == 0:
                    weapon = str(tag.get_text())
                    weapon_dict[heading][weapon] = \
                        dict(zip(attrib_list, attrib_info))
                else:
                    weapon_dict[heading][weapon][attrib_list[idx - 1]] \
                        = str(tag.get_text())
                idx = (idx + 1) % 5

    return weapon_dict

if __name__ == "__main__":
    main()
