import requests
from bs4 import BeautifulSoup

target_link = 'https://boston.craigslist.org/search/sof'
target_soup = BeautifulSoup(requests.get(target_link).content, 'html.parser')


def scraper(soup):
    jobs = [li.p.a for li in soup.find_all('li', class_='result-row')]
    for job in jobs:
        print('Job: ' + job.text)
        print('URL: ' + job['href'] + '\n')


scraper(target_soup)
