# import urllib.request
# from bs4 import BeautifulSoup

# def get_html(url):
# 	response = urllib.request.urlopen(url)
# 	return response.read()

# def main():
# 	print(get_html('http://www.bashinform.ru/news/'))


# if __name__ == '__main__':
# 	main()
import random
import requests

agents = [
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)']
headers = {"User-Agent":random.choice(agents)}

url = "http://bashinform.ru/news/"
response = requests.get(url,headers=headers)
print(response.text)