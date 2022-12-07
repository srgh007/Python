import re
import urllib.request

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
# print(ua.chrome)
header = {"User-Agent": str(ua.chrome)}
# print(header)


url = "https://www.sport.ru/football/chm-2022/Playoff/"

# htmlContent = requests.get(url, headers=header)
# print(htmlContent)


req = urllib.request.Request(url, data=None, headers=header)

f = urllib.request.urlopen(req)

html = f.read()

soup = BeautifulSoup(html, "html.parser")
news = soup.find_all(class_=re.compile("gs3f0-s[1-9]"))
f = open("out.txt", "w", encoding="utf-8")
try:
    for l in news:
        # if l.get_text() in ":1234567890":
        #     f.write(l.get_text())
        # else:
        f.write(l.get_text() + "\n")
finally:
    f.close()
# print(news)
