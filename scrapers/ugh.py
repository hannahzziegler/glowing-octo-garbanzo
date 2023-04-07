import csv
import datetime
import requests
from bs4 import BeautifulSoup
import itertools
import pandas as pd
from datetime import datetime

# this works, but it only pulls down the "A" letters because the directory is
# split into separate pages per each letter

page = 0

big_list = []

# A
a_list = []
while page <= 870:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=A&offset={page}"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 4:
            employee_name = cells[0].get_text().strip()
            agency_name = cells[1].get_text().strip()
            office = cells[2].get_text().strip()
            phone = cells[3].get_text().strip()
            a_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    big_list.append(a_list)

b_list = []
while page <= 2010:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=B&offset={page}"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 4:
            employee_name = cells[0].get_text().strip()
            agency_name = cells[1].get_text().strip()
            office = cells[2].get_text().strip()
            phone = cells[3].get_text().strip()
            b_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    big_list.append(b_list)

print(a_list)
print(b_list)
print(big_list)
