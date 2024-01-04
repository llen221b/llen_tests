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


