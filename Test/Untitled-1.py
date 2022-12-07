import urllib.request

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
# print(ua.chrome)
header = {"User-Agent": str(ua.chrome)}
# print(header)


url = "https://matchtv.ru/football/worldcup"

# htmlContent = requests.get(url, headers=header)
# print(htmlContent)


req = urllib.request.Request(url, data=None, headers=header)

f = urllib.request.urlopen(req)

html = f.read()

soup = BeautifulSoup(html, "html.parser")
news = soup.find_all("div")
f = open("out.txt", "a", encoding="utf-8")
try:
    for l in news:
        f.write(l.get_text())
finally:
    f.close()
# print(news)
