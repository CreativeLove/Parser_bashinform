#!/usr/bin/env python3
import random
import requests
import csv
from bs4 import BeautifulSoup

def get_html(url):
    agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)']
    headers = {"User-Agent":random.choice(agents)}
    response = requests.get(url,headers=headers)
    return response.text

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('article')
    rows = []
    for article in articles:
        names = article.find_all('a', 'name')
        for i in range(len(names)):
            link = names[i].attrs['href']
            if (link[0] == '/'):
                    link = 'http://www.bashinform.ru' + link
            rows.append((names[i].get_text(), link))
            print(names[i].get_text())
            print(link)
    return rows

def printCSV(rows):
    f = open("bashinform.csv", "wb")
    wr = csv.writer(f, delimiter=";")
    for i in range(len(rows)):
        wr.writerow({wr[i].first, wr[i].second})
    f.close()
    

def main():
    printCSV(parse(get_html('http://www.bashinform.ru')))


if __name__ == '__main__':
    main()
