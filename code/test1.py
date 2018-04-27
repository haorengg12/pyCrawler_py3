# soul land : the legend of the Dragon King
# python3
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm, trange

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}  # 代理
url = 'http://www.tycqxs.com%s'  # 小说网址
local_path = '../book%s'


def linkstart():
    url_l = url % ('/48_48093')  # 龙王传说
    res = requests.get(url=url_l, proxies=proxies)
    return res


def download(link, title):
    res = requests.get(url=link, proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    article = soup.find('div', id="content").text
    bookname = soup.find('div', {"class": 'bookname'}).h1.text
    path = local_path % ('/' + title + '.txt')
    with open(path, 'ab+') as f:  # 写入文件
        f.write((bookname + '\n' + article).encode('utf-8'))
        f.close()


def newDir():  # 新建文件夹
    while not os.path.exists(local_path % ''):
        os.makedirs(local_path % '')


def stddown(book, title):
    for i in trange(len(book)):
        # print('第' + str(i) + '章')
        download(url % (book[i]['href']), title)


if __name__ == '__main__':  # main function
    res = linkstart()
    soup = BeautifulSoup(res.content, 'html.parser')
    bklist = soup.find('div', id='list')
    title = soup.find('meta', property="og:title")['content']  # 标题
    newDir()
    book = bklist.findAll('a')
    print('Start!')
    os.system("cls")
    stddown(book, title)
    os.system("cls")
    print('Finish!')
