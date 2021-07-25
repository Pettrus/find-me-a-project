from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.hackster.io/projects?ref=topnav&sort=published')
r.html.render()
grid_elements = r.html.find('.cards__wrapper__3CdjF')

for element in grid_elements:
    description = element.find('span')
    print(description)
    break