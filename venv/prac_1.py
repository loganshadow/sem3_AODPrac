import requests
from bs4 import BeautifulSoup

URL = 'https://zayman.ru/currency/usd?range=10year'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

def get_html(url, params = None):
    r = requests.get(url, headers = header, params=params)
    return  r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    lines = soup.find("table", class_="currency-table").find_all('tr')
    months = []
    for line in lines[1:]:
        months.append({
            "date": line.find('a').get_text(),
            "value": line.find('strong').get_text()
        })
    print(months)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.status_code)
        get_content(html.text)
    else:
        print("Error")

parse()