import requests
from bs4 import BeautifulSoup

base_site = 'https://editorial.rottentomatoes.com/guide/inspiring-movies/'

#check the response
response = requests.get(base_site)
# print(response)

html = response.content
soup = BeautifulSoup(html, 'html.parser')

#export html to a file
# with open ('rotten_tomatoes_html_parser.html', 'wb') as file:
#     file.write(soup.prettify('utf-8'))

divs = soup.find_all('div', {'class': 'col-sm-18 col-full-xs countdown-item-content'})
# print(divs)

headings = [div.find('h2') for div in divs]
# print(headings[0])

#extract movie names
movie_names = [heading.find('a').string for heading in headings]
print(movie_names)

#extract years
years = [heading.find('span', class_ = 'start-year').string for heading in headings]
#remove brackets and convert years to integers
years = [year.strip('()') for year in years]
years = [int(year) for year in years]
print(years)

#extract score
scores = [heading.find('span', class_ = 'tMeterScore').string for heading in headings]
print(scores)

#extract critics consensus
consensus = [div.find('div', {'class': 'info critics-consensus'}) for div in divs]
common_phrase = 'Critics Consensus:'
common_len = len(common_phrase)
consensus_text = [con.text[common_len:] if con.text.startswith(common_phrase) else con.text for con in consensus]
print(consensus_text)

#extract directors
directors = [div.find('div', class_ = 'director') for div in divs]
dir = [director.find('a').string for director in directors]
print(dir)

#extract cast info
cast_info = [div.find('div', class_ = 'cast') for div in divs]
cast = []
for c in cast_info:
    cast_links = c.find_all('a')
    cast_names = [link.string for link in cast_links]
    cast1 = ','.join(cast_names)
    result = cast.append(cast1)
print(result)


print(cast_names)
