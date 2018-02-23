import requests
import csv
from bs4 import BeautifulSoup


# Получаем адрес, который будем парсить
# Возвратим все элементы (теги) страницы
def get_html(url): 
    agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url,headers = agent)
    return response.text



# Получаем внутреннее содержимое страницы
def parse(html):
    soup = BeautifulSoup(html, 'html.parser') # Подключаем Html parser
    articles = soup.find_all('a', 'name') # Находим все теги a с классом name (article)

    for article in articles:
    	name = article.text    # Содержимое article  
    	href = article.attrs['href']    # Ссылка на article  
    	if (href[0:5] == "/news"):
            print(name)
            print(href)
            data = [name, href]
            printCSV(data)
            print("ololo")

# Выводит в формат CSV
def printCSV(data):
    wr = csv.writer(f, delimiter=";")   
    wr.writerow(data)
    

def main():
    with open("bashinform.csv", "w", newline="") as f:
           
        parse(get_html('http://www.bashinform.ru'))
    f.close()
    # printCSV(["One", "Two", "Three"])


if __name__ == '__main__':
    main()

