# in a worst case scenario, I can go letter-by-letter just like I did with this
# "a" directory example and then compile all of the lists of lists into the same
# final dataframe, which would be the one that is monitered in this script.
# it is painfully inefficient, but just knowing that I have at least one working
# scraper that can be repurposed for each letter and have functions for each
# that run weekly/etc.

# tried to code this out on saturday morning, getting frustrated, moving on to
# just getting the vacancies to work for now

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

all_employees_data = []

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
    all_employees_data.append(a_list)

    # B
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
    all_employees_data.append(b_list)

    # C
c_list = []
while page <= 1695:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=C&offset={page}"
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
            c_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(c_list)

    # D

d_list = []
while page <= 1200:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=D&offset={page}"
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
            d_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(d_list)

    # E

e_list = []
while page <= 450:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=E&offset={page}"
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
            e_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(e_list)

# F

f_list = []
while page <= 915:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=F&offset={page}"
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
            f_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(f_list)

# G

g_list = []
while page <= 1125:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=G&offset={page}"
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
            g_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(g_list)

# H

h_list = []
while page <= 1605:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=H&offset={page}"
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
            h_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(h_list)

# I

i_list = []
while page <= 150:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=I&offset={page}"
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
            i_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(i_list)

    # J

j_list = []
while page <= 780:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=J&offset={page}"
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
            j_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(j_list)

    # K

k_list = []
while page <= 840:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=K&offset={page}"
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
            k_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(k_list)

    # L

l_list = []
while page <= 1065:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=L&offset={page}"
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
            l_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(l_list)

    # M
m_list = []
while page <= 2100:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=M&offset={page}"
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
            m_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(m_list)

    # N
n_list = []
while page <= 450:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=N&offset={page}"
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
            n_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(n_list)

    # O
o_list = []
while page <= 450:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=O&offset={page}"
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
            o_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(o_list)

    # P
p_list = []
while page <= 1050:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=P&offset={page}"
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
            p_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(p_list)

    # Q
q_list = []
while page <= 60:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=Q&offset={page}"
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
            q_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(q_list)

    # R
r_list = []
while page <= 1125:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=R&offset={page}"
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
            r_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(r_list)

    # S
s_list = []
while page <= 2370:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=S&offset={page}"
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
            s_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(s_list)

    # T
t_list = []
while page <= 840:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=T&offset={page}"
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
            t_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(t_list)

    # U
u_list = []
while page <= 60:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=U&offset={page}"
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
            u_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(u_list)

    # V
v_list = []
while page <= 585:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=V&offset={page}"
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
            v_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(v_list)

    # W
w_list = []
while page <= 1395:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=W&offset={page}"
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
            w_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(w_list)

    # X
x_list = []
while page <= 15:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=X&offset={page}"
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
            x_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(x_list)

    # Y
y_list = []
while page <= 150:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=Y&offset={page}"
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
            y_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(y_list)

    # Z
z_list = []
while page <= 165:
    url = f"https://www.doit.state.md.us/phonebook/IndListing.asp?FirstLetter=Z&offset={page}"
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
            z_list.append(
                [employee_name, agency_name, office, phone])
    page = page + 15
    all_employees_data.append(z_list)

print(z_list)
print(t_list)
print(e_list)
print(all_employees_data)

# df = pd.DataFrame(all_employees_data, columns=[
# 'employee_name', 'agency_name', 'office', 'phone_number'])
# print(df)

# csv_file = open("md_employees" +
#                str(datetime.now().strftime('%Y_%m_%d')) + ".csv", "w")
# writer = csv.writer(csv_file)
# writer.writerow(["employee_name", "agency_name", "office", "phone"])
# writer.writerows(all_employees_data)


# if __name__ == "__main__":
#    scrape_by_letter()
