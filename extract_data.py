# pip install requests
# pip install beautifulsoup4 lxml
import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IPhone'
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')
table = soup.find('table', class_='wikitable')
# [1::1] means start for index1
rows = table.find_all('tr')[1::1]
print(table)
