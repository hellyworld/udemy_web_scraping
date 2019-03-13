import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
#
# user_agent = UserAgent
# headers = {'user-agent': user_agent.chrome}
target_link = 'https://codingbat.com'


def soup_maker(link):
    # return BeautifulSoup(requests.get(link).content, 'html.parser')
    return BeautifulSoup(requests.get(link).content, 'lxml')


first_soup = soup_maker(target_link)
categories_links = [target_link + div.a['href'] for div in first_soup.find_all('div', class_='summ')]

for category_link in categories_links:
    target_soup = soup_maker(category_link)
    div = target_soup.find('div', class_='indent')
    problems_links = [target_link + td.a['href'] for td in div.table.find_all('td')]

    for problem_link in problems_links:
        final_soup = soup_maker(problem_link)
        question = final_soup.find('div', class_='indent')
        print(question.table.div.string)

        break

    break

