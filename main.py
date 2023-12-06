from bs4 import BeautifulSoup
import requests
import os
import json
from selenium import webdriver
webBrowser = webdriver.Firefox()
with open(fr'{os.getcwd()}\film.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

for index in data:
    try:
        id_video = data[index]["ID"]
        url = f'https://m.ok.ru/video/{id_video}'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        link = soup.find('a', {'class': 'outLnk fll vdo tbcont js-click'}).get('href')
        webBrowser.execute_script(f"window.open('{link}')", 'new window')
    except:
        continue
