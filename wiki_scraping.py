import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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

#find all main articles under headers
div_links = []
div_notes = soup.find_all('div', {'role': 'note'})

for div in div_notes:
    anch = div.find_all('a')

    for a in anch:
        div_links.append(a)
note_urls = [urljoin(base_site, l.get('href') )for l in div_links]
print(note_urls)
