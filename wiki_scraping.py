import requests
from bs4 import BeautifulSoup

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)

html = response.content

soup = BeautifulSoup(response.content, features="html.parser")

#exporting html to a file
with open ("wiki_response.html", "wb") as file:
    file.write(soup.prettify('utf-8'))

#find href attribute
for att in soup.find_all('a'):
    href = att.get('href')
    text = att.string
    print('Link:', href, 'Text:', text)


