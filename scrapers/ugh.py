import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

# Define the base URL
base_url = "https://www.doit.state.md.us/phonebook/indlisting.asp?letter={}&offset={}"
letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

for letter in letters:
    offset = 0
    page_links = []
    while True:
        url = base_url.format(letter, offset)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all(
            "a", href=lambda href: href and letter in href and "offset" in href)
        page_links.extend(links)
        next_link = soup.find("a", {"title": "Next"})
        if not next_link:
            break
        offset += 15
    print("Page links for {}: {}".format(letter, page_links))
