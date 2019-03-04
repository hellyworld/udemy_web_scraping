import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
header = {'user-agent': ua.chrome}
page = requests.get('https://boston.craigslist.org/search/sof', headers=header)

soup = BeautifulSoup(page.text, "lxml")

info = soup.find_all("p", attrs={"class": "result-info"})

for i in info:
    first = i.find('a')
    print("Job", " =  ", first.string)
    print("Url", " =  ", first["href"], "\n")
