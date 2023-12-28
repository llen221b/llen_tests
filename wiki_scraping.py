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

#get all the text of these articles and put it in dictionary
par_text = []

i = 0
for url in note_urls:

    note_resp = requests.get(url)

    if note_resp.status_code == 200:
        print('URL #{0}: {1}'.format(i+1, url))
    else:
        print('Status code {0}: Skipping URL #{1}: {2}'.format(note_resp.status_code, i+1,url))
        i = i+1
        continue

    note_html = note_resp.content
    note_soup = BeautifulSoup(note_html, 'lxml')
    note_pars = note_soup.find_all('p')
    text = [p.text for p in note_pars]
    par_text.append(text)
    i = i+1

page_text = [''.join(text) for text in par_text]

url_to_text = dict(zip(note_urls, page_text))
print(url_to_text['https://en.wikipedia.org/wiki/Index_of_music_articles'])
