import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

# the rest of this initial scraper is in a jupyter notebook because I found that to be the easiest location for troubleshooting different issues
# I'll probably move the code over here once I have a better graps of what's working/not after spring break
