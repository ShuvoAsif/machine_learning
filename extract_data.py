# pip install requests
# pip install beautifulsoup4 lxml
# [1::1] means start for index1
import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IPhone'
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')
table = soup.find('table', class_="wikitable")
# print(table)
rows = table.find_all('tr')[1::1]

for row in rows:
    data = row.find_all(['th', 'td'])

    try:
        version_text = data[0].a.text.split('/')[0]
        version_text = ''.join(i for i in version_text if i.isdigit())
        version = int(version_text)
        print(version)
    except:
        pass
