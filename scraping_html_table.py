import requests
from bs4 import BeautifulSoup
import pandas as pd

base_site = 'https://en.wikipedia.org/wiki/List_of_national_capitals_by_population'

r = requests.get(base_site)
html = r.content
soup = BeautifulSoup(html, 'lxml')
table = soup.find_all('table')[1]
# print(table)
table.find_all('tr')[0].contents
capitals = [row.contents[3].text for row in table.find_all('tr')]
print(capitals)

tables = pd.read_html(base_site)
print(tables)
