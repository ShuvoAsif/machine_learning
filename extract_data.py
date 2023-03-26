# pip install requests
import requests
url = 'https://en.wikipedia.org/wiki/IPhone'
res = requests.get(url).text
print(res)
