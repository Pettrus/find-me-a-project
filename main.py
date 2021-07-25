import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.hackster.io/projects?ref=topnav&sort=published")
soup = BeautifulSoup(page.content, 'html.parser')
grid_elements = soup.find_all('div', class_='cards__wrapper__3CdjF')

for element in grid_elements:
    description = element.find('span').get_text()
    print(description)
    break