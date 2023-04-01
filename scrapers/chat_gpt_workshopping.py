# chatgpt's suggestion for getting every single page URL for each letter is
# not! working! at all, but keeping here to refer back to

import requests
from bs4 import BeautifulSoup

# Define the base URL
base_url = 'https://www.doit.state.md.us/phonebook/indlisting.asp'

# Initialize an empty list to store the data
data = []

# Loop through each page (A to Z)
for letter in range(65, 91):  # ASCII codes for A to Z
    # Construct the initial URL
    url = f'{base_url}?letter={chr(letter)}&offset=0'
    # Send a request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the total number of pages for this letter
    page_links = soup.find_all(
        'a', {'href': lambda href: href and f'letter={chr(letter)}&offset=' in href})
    if page_links:
        last_page_num = int(page_links[-1]['href'].split('=')[-1]) // 15
        print(page_links)
    else:
        last_page_num = 0
    # print(page_links)

    # Loop through each page for this letter
    for page_num in range(last_page_num + 1):
        # Construct the URL for this page
        offset = page_num * 15
        url = f'{base_url}?letter={chr(letter)}&offset={offset}'
        print(url)
        # Send a request to the URL
        response = requests.get(url)
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

# Print the data
print(data)
