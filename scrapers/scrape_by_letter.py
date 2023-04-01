# in a worst case scenario, I can go letter-by-letter just like I did with this
# "a" directory example and then compile all of the lists of lists into the same
# final dataframe, which would be the one that is monitered in this script.
# it is painfully inefficient, but just knowing that I have at least one working
# scraper that can be repurposed for each letter and have functions for each
# that run weekly/etc.

import csv
import datetime
import requests
from bs4 import BeautifulSoup
import itertools
import pandas as pd

# this works, but it only pulls down the "A" letters because the directory is split into separate pages per each letter
page = 0
a_table_data = []
while page != 870:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=A&offset={page}"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all("td")
        row_data = []
        for cell in cells:
            row_data.append(cell.text.strip())
            a_table_data.append(row_data)
    page = page + 15
print(a_table_data)
