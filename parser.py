#!/usr/bin/env python3 
import random 
import requests 
import csv
import datetime
from bs4 import BeautifulSoup 

# Получение HTML кода
def get_html(url): 
    agents = [ 
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)', 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'] 
    headers = {"User-Agent":random.choice(agents)} 
    response = requests.get(url,headers=headers)
    return response.text 

# Получение массива данных по HTML коду
def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    rows = [] # массив пар (название, краткое содержание, ссылка)

    articles = soup.find_all('article')
    for article in articles:
        if (len(article.find_all('h2')) == 0):
            continue
        name = article.find_all('h2')[0].find_all('a')[0].text
        link = article.find_all('h2')[0].find_all('a')[0].attrs['href']
        trailer = article.find_all(class_='trailer')[0].find_all('p')[0].text
        rows.append((name, trailer, link))
        print(name)
        print(trailer)
        print(link)
        print('--------')
            
    return rows

# Запись данных в csv файл
def printCSV(rows, writer):    
    for i in range(len(rows)):
        writer.writerow(rows[i])

# Возвращает кол-во дней в месяцах
def getDays():
    days = {1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31}
    return days
    
def main():
    rows = []
    year = 2018
    month = 1
    day = 23
    days = getDays()
    curDay = datetime.datetime.now().day
    curMonth = datetime.datetime.now().month
    curYear = datetime.datetime.now().year
    with open("bashinform.csv", "w") as csvFile:
        csvWriter = csv.writer(csvFile, quotechar=';')
        while True:
            print(str(year)+' '+str(month)+' '+str(day))
            printCSV(parse(get_html('http://www.bashinform.ru/news-list-2/' + str(year) + "/" + str(month).zfill(2) + '/' + str(day).zfill(2) + '/')), csvWriter)
            if (year == curYear and month == curMonth and day == curDay):
                break
            day+=1
            if (day > days[month] and ((year % 4 != 0 or month != 2) or (year % 4 == 0 and month == 2 and day == 30))):
                day = 1
                month += 1
            if (month > 12):
                month = 1
                year += 1
        csvFile.close()
        
if __name__ == '__main__': 
    main()
