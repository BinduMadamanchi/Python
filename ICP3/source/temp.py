import requests
from bs4 import BeautifulSoup
import os
url="https://en.wikipedia.org/wiki/Deep_learning"
source_code=requests.get(url)
plain_text=source_code.text
soup = BeautifulSoup(plain_text,"html.parser")
print(soup.title)
print(soup.find_all('a'))
for link in soup.find_all('a'):
    print(link.get('href'))
