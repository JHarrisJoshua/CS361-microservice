"""Program represents a microservice to a video game companion tool.
The microservice provides data related to in-game items and item 
attributes by scraping a community wiki page."""
import urllib.request
from bs4 import BeautifulSoup
import json

def main() -> None:
    """Checks for request, scrapes html, and results data"""
    # Check for request
    while True:
        with open("pipe.txt", "r") as infile:
            line = infile.read()
        
        if line == "Get Weapon Stats":
            print("Received Request")
            # Get data
            stats = scrape_stats()
        
            print("Posting data")
            with open("weapon_stats.json", 'w') as outfile:
                json.dump(stats, outfile, indent=4)

            print('Sending Response')
            with open("pipe.txt", "w") as file:
                file.write("weapon_stats.json")
            print('Response Sent')

def scrape_stats():
    """Retrieves information from wiki page using
    beautiful soup library.
    """
    result = list()
    query = 'http://dnd5e.wikidot.com/weapons/'

    # Open URL, read HTML, and scrape tags
    #   https://beautiful-soup-4.readthedocs.io/en/latest/
    url = query
    html_page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    for tag in soup.find_all(['h1', 'th', 'td']):
        # Minor clean-up of html, otherwise, provides raw html data
        result.append(str(tag).replace("\u00a0"," "))
    return result

if __name__ == "__main__":
    main()
