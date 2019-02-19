import requests
from bs4 import BeautifulSoup
import pandas as pd
i = 1
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")

source = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")

soup = BeautifulSoup(source.content, "html.parser")

beauty = soup.find_all('table', class_ ='wikitable')[0]
file = open('states.text', 'a')
rows = beauty.findAll('tr')[10:]
for tr in rows:
    print(f"{i} State - {tr.th.a.string}")
    print(f"   Capital -{cols[1].text}")
    file.write(f"{i} State - {tr.th.a.string}")
    file.write(f"   Capital -{cols[1].text}")
    i=i+1