# this is a working scraper that only pulls down the state employee vacancies,
# rather than all of the data. so we have *something* to work with!!!!
# the main thing I wanted to figure out here was making it so I don't have to
# hard-code the number of x15 multiples

import csv
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = 0
table_data = []
updated_vacancies = []
while page <= 330:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=vacant&Submit=Search&offset={page}"
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
            table_data.append([employee_name, agency_name, office, phone])
    page = page + 15

print(table_data)

df = pd.DataFrame(table_data, columns=[
                  'employee_name', 'agency_name', 'office', 'phone_number'])
print(df)

csv_file = open("md_employees" + (time.strftime('%Y_%m_%d')) + ".csv", "w")
writer = csv.writer(csv_file)
writer.writerow(["employee_name", "agency_name", "office", "phone"])
writer.writerows(table_data)
