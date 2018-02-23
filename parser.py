import requests
import csv
from bs4 import BeautifulSoup




url = 'http://www.bashinform.ru'
f = open("bashinform.csv", "w", newline="")




# Получаем адрес, который будем парсить
# Возвратим все элементы (теги) страницы
def get_html(url): 
    agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url,headers = agent)
    return response.text



# Получаем внутреннее содержимое страницы
def parse(html):
    soup = BeautifulSoup(html, 'html.parser') # Подключаем Html parser

    name_mass = soup.select('article > h2 > a') # Находим все названия статей
    description_mass = soup.select('article > .trailer > p') # Находим все теги a

    for i in range(len(name_mass)):
        name = name_mass[i].text
        href = name_mass[i].attrs['href']
        description = description_mass[i].text
        if (href[0:6] == "/news/"):
            print(name) # Название статьи 
            print(url + href) # Ссылка на статью
            print(description)
            data = [name, url + href, description]
            printCSV(data)
            print("")   



# Выводит в формат CSV
def printCSV(data):
    wr = csv.writer(f, delimiter=";")   
    wr.writerow(data)



def main():
    printCSV(['Название', 'Ссылка', 'Краткое содержание'])
    for i in range(1, 23):
        print(i)
        parse(get_html('http://www.bashinform.ru/news-list-2/2018/02/' + str(i) + '/'))
    f.close()    


if __name__ == '__main__':
    main()

