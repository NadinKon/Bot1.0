import requests
import random
from bs4 import BeautifulSoup as b

url = 'https://www.anekdot.ru/last/good'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


list_jokes = parser(url)
random.shuffle(list_jokes)

