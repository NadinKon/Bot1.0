import requests
from bs4 import BeautifulSoup as b
import re

url = 'https://moigoroskop.org/goroskop/'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    #advices = soup.find_all('div', class_='col-md-9 col-sm-9')
    g = soup.find_all("p")
    day = re.sub('<[^>]*>', '', str(g[0]))
    advice = re.sub('<[^>]*>', '', str(g[1]))
    return [advice, day]


list_advice = parser(url)

