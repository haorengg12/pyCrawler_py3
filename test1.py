# 斗罗大陆 龙王传说
import requests
from bs4 import BeautifulSoup

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}
url = 'http://www.tycqxs.com%s'  # 小说网址
res = requests.get(url=url, proxies=proxies)
soup = BeautifulSoup(res.content, 'html.parser')
bklist = soup.find('div', id='list')
book = bklist.findAll('a')
for i in range(len(book)):
    print(book[i]['href'], book[i].text)
