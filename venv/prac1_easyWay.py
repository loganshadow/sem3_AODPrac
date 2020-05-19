import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.audit-it.ru/currency/daily_curs.php?monthStart=0&yearStart=2010&monthEnd=0&yearEnd=2020&currency=USD&currencyTable=USD%2CEUR%2CCZK'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}


def get_html(url, params = None):
    r = requests.get(url, headers = header, params=params)
    return  r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    lines = soup.find('tbody').find_all('tr')
    months = []
    for line in lines:
        cols = line.find_all('td')
        months.append({
            'date': cols[0].text,
            'value': cols[1].text.strip()
        })
    return months


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.status_code)
        content = get_content(html.text)
    else:
        print("Error")
    return content


def save(data, path):
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(('date', 'value'))
        writer.writerows(
            (item['date'], item['value']) for item in data
        )


data = parse()
data = reversed(data)
save(data, 'usd_rubles.csv')