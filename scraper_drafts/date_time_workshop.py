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

# Define the directory where the CSV files are stored
csv_dir = '../'

# Get the current date and the date of the previous day
today = date.today()
yesterday = today - timedelta(days=1)

# Construct the file names for the current and previous CSV files
current_file_name = f"md_employees{today.strftime('%Y_%m_%d')}.csv"
previous_file_name = f"md_employees{yesterday.strftime('%Y_%m_%d')}.csv"

# Construct the file paths for the current and previous CSV files
current_file_path = os.path.join(csv_dir, current_file_name)
previous_file_path = os.path.join(csv_dir, previous_file_name)

# Use filecmp to compare the two files
are_files_equal = filecmp.cmp(current_file_path, previous_file_path)

# If the files are different, print the differences
if not are_files_equal:
    with open(current_file_path, 'r') as current:
        with open(previous_file_path, 'r') as previous:
            current_csv = csv.reader(current)
            previous_csv = csv.reader(previous)
            for current_row, previous_row in zip(current_csv, previous_csv):
                if current_row != previous_row:
                    print(f'Difference found: {current_row} vs {previous_row}')
                else:
                    print('No changes to report!')

# Comparing the files


today = date.today()
yesterday = today - timedelta(days=1)

current_file_name = f"md_employees{today.strftime('%Y_%m_%d')}.csv"
previous_file_name = f"md_employees{yesterday.strftime('%Y_%m_%d')}.csv"

yesterday_data = pd.DataFrame(f"md_employees{yesterday.strftime('%Y_%m_%d')}.csv", columns=[
                              'employee_name', 'agency_name', 'office', 'phone_number'])
print(yesterday_data)

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