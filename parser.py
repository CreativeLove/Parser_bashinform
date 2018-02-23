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
    articles = soup.select('article > h2 > a') # Находим все теги a с классом name (article)

    for article in articles:
    	name = article.text    # Название  
    	href = article.attrs['href']    # Ссылка на article  
    	if (href[0:6] == "/news/"):
            print(name)
            print(url + href)
            data = [name, url + href]
            printCSV(data)
            print("")



# Выводит в формат CSV
def printCSV(data):
    wr = csv.writer(f, delimiter=";")   
    wr.writerow(data)



def main():
    for i in range(1, 23):
        print(i)
        parse(get_html('http://www.bashinform.ru/news-list-2/2018/02/' + str(i) + '/'))
    f.close()    


if __name__ == '__main__':
    main()

