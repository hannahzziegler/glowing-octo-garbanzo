# using this script to try to fix how the pages can be scraped through both the
# letter values in the URL and the specific page values (that are incremented
# by 15)

# worked on this for most of saturday and am a bit stuck, so planning to keep
# pounding the pavement with it on sunday/monday and definitely ask about it in
# class

# each URL number (855, 856, 857) corresponds to a specific entry into the table.
# thinking of ways to target those within the scrape for the tr tags within the
# broader "for loop" associated with each letter
# this number corresponding to every entry into the table on every page makes
# sense -- but I'm confused about how it actually works/can be accessed to
# make the URL parsing task and general scraping process easier to automate.

import requests
from bs4 import BeautifulSoup

# Define the base URL
base_url = 'https://www.doit.state.md.us/phonebook/indlisting.asp'

# Initialize an empty list to store the data
data = []
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
page_num = 0
# Loop through each page (A to Z)
for letter in alpha:
    page_url = f"{base_url}?letter={alpha}&offset={page_num}"
    while True:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all tables on the page
        tables = soup.find_all('table')
        # Loop through each table
        for table in tables:
            # Find all rows in the table
            rows = table.find_all('tr')
            for row in rows:
                # Find all cells in the row
                cells = row.find_all('td')
                # Extract the data from each cell
                if len(cells) == 4:
                    # Ignore the header row
                    name = cells[0].get_text().strip()
                    title = cells[1].get_text().strip()
                    phone = cells[2].get_text().strip()
                    email = cells[3].get_text().strip()
                    # Append the data to the list
                    data.append([name, title, phone, email])
        next_link = soup.find(
            'a', {'href': lambda href: href and '/phonebook/indlisting.asp?offset=' in href})
        #next_link = soup.find('a', {'href': 'Next'})
        if next_link is not None:
            # Increment the page number and construct the new URL
            page_num += 15
            url = f'{base_url}?letter={chr(letter)}&offset={page_num}'
        else:
            # No more pages, break out of the loop
            break

# Print the data
for item in data:
    print(item)


#    # Find the pagination links on the page
    #pagination = soup.find_all('td', text=pattern2)
    #soup.find('td', {'align': 'center'})
    # if pagination is not None:
    #   links = pagination.find_all('a')
    #   num_pages = len(links) + 1
    # else:
    #   num_pages = 1

    # Loop through each page
    # for page in range(1, num_pages + 1):
    #   # Construct the URL for the page
    #  if page == 1:
    #     page_url = base_url + '?letter=' + chr(letter)
    # else:
    #     page_url = base_url + '?letter=' + \
    #        chr(letter) + '&page=' + str(page)
    # response = requests.get(page_url)
    # soup = BeautifulSoup(response.text, 'html.parser')
