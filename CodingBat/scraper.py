import requests
from bs4 import BeautifulSoup

target_link = 'https://codingbat.com'


def soup_maker(link):
    return BeautifulSoup(requests.get(link).content, 'html.parser')


target_soup = soup_maker(target_link)
categories_links = [target_link + div.a['href'] for div in target_soup.find_all('div', class_='summ')]

print(categories_links)
print(soup_maker('https://codingbat.com/java/Warmup-1').find_all('indent'))
problems_links = []
for category_link in categories_links:
    target_soup = soup_maker(category_link)
    target = target_soup.find('div', class_='indent')
    for td in target.find_all('td'):
        print(td)
    # problems_links.append([target_link + table.tbody.tr.td.a['href'] for table in target_soup.find_all('table')])
    # print(problems_links)

# print(problems_links)
