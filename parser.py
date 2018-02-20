import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def main():
	print(get_html('http://www.bashinform.ru/longread/gornolyzhka/'))
	#print(get_html('https://www.youtube.com/watch?v=3hgkiDAaSQs'))


if __name__ == '__main__':
	main()