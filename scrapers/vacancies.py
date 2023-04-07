# this is a working scraper that only pulls down the state employee vacancies,
# rather than all of the data. so we have *something* to work with!!!!
# the main thing I wanted to figure out here was making it so I don't have to
# hard-code the number of x15 multiples

import csv
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from slack import WebClient
from slack.errors import SlackApiError
from datetime import date, timedelta
import filecmp

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
total_vacancies = len(df. index)

csv_file = open("md_employees" + (time.strftime('%Y_%m_%d')) + ".csv", "w")
writer = csv.writer(csv_file)
writer.writerow(["employee_name", "agency_name", "office", "phone"])
writer.writerows(table_data)

# Comparing the files

today = date.today()
yesterday = today - timedelta(days=1)

current_file_name = f"md_employees{today.strftime('%Y_%m_%d')}.csv"
previous_file_name = f"md_employees{yesterday.strftime('%Y_%m_%d')}.csv"

#current_file_path = os.path.join(csv_dir, current_file_name)
#previous_file_path = os.path.join(csv_dir, previous_file_name)

# Use filecmp to compare the two files
are_files_equal = filecmp.cmp(current_file_name, previous_file_name)

# If the files are different, print the differences
if not are_files_equal:
    with open(current_file_name, 'r') as current:
        with open(previous_file_name, 'r') as previous:
            current_csv = csv.reader(current)
            previous_csv = csv.reader(previous)
            if current_csv == previous_csv:
                print('No new data found')
            else:
                print('New data found!')

                # if current_row != previous_row:
                #    print(f'Difference found: {current_row} vs {previous_row}')
                # else:
                #    print('No changes to report!')

#df.to_csv('data.csv', index=False)
# read the existing CSV file into a DataFrame called `old_data`
#old_data = pd.read_csv('data.csv')
# compare the two DataFrames to check for new data
# if old_data.equals(df):
#    print('No new data found')
# else:
#    print('New data found!')
#    # append the new data to the CSV file
#    all_data = pd.concat([old_data, df], ignore_index=True)
#    all_data.to_csv('data.csv', index=False)
#df.to_csv('data.csv', index=False)

slack_token = os.environ.get('SLACK_API_TOKEN')
client = WebClient(token=slack_token)

msg = f"There are currently {total_vacancies} state employee vacancies."
try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True,
        unfurl_media=True
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
