# first try -- will eventually be updated to show final scraper that I use for
# the bot, but right now is just a bit messy. full workflow that I've been piecing
# together is shown in the other named .py scrapers within this folder.

import csv
import datetime
import requests
from bs4 import BeautifulSoup
import itertools
import pandas as pd

# this works, but it only pulls down the "A" letters because the directory is split into separate pages per each letter
#page = 0
#table_data = []
# while page != 870:
#    url = f"https://www.doit.state.md.us/phonebook/indlisting.asp?offset={page}"
#    response = requests.get(url)
#    html = response.content
#    soup = BeautifulSoup(html, features="html.parser")
#    table = soup.find('table')
#    rows = table.find_all('tr')
#    for row in rows:
#        cells = row.find_all("td")
#        row_data = []
#        for cell in cells:
#            row_data.append(cell.text.strip())
#            table_data.append(row_data)
#    page = page + 15
#    print(table_data)


# https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=A&offset=15

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
page = 0
base_url = 'https://www.doit.state.md.us/phonebook/IndListing.asp'
table_data = []
for letter in alpha:
    while page != -1:
        url = f'{base_url}?FirstLetter={alpha}&offset={page}'
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
                table_data.append(row_data)
    page = page + 15
print(table_data)

# Extract information from each page
# for item in soup.find_all('div', {'class': 'item'}):
#    title = item.find('h2').text.strip()
#    description = item.find('p').text.strip()
#    # Do something with the extracted information

# making things more readable

# df = pd.DataFrame(table_data, columns=[
# 'employee_name', 'agency_name', 'office', 'phone_number'])
# print(df)
