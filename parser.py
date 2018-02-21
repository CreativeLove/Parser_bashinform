#!/usr/bin/env python3
import random
import requests
from bs4 import BeautifulSoup

def get_html(url):
    agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)']
    headers = {"User-Agent":random.choice(agents)}
    response = requests.get(url,headers=headers)
    return response.text

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article')
    for article in articles:
        names = article.find_all('a', 'name')
        if (len(names) > 0):
            print('-----------------')
            for i in range(len(names)):
                print(names[i].text)
                print(names[i].attrs['href'])

def main():
    print(parse(get_html('http://www.bashinform.ru')))


if __name__ == '__main__':
    main()
