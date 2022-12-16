import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

request = requests.session()

google = request.get('https://www.google.com.tw/',headers=headers)
soup = BeautifulSoup(google.text,'html.parser')
print(soup.prettify()) 

payload = {"q":"123"}

google = request.get('https://www.google.com.tw/search?',headers=headers,params=payload)
print(google.url)
soup = BeautifulSoup(google.text,'html.parser')

# 所有的超連結
a_tags = soup.find_all('a')
for tag in a_tags:
  # 輸出超連結的文字
  print(tag.string)