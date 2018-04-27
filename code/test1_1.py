# coding=utf-8
# 用来进行文件测试
import os
import requests
from bs4 import BeautifulSoup


def testPath(tpath, tmode):  # 测试文件读写权限
    print(os.access(tpath, tmode))  # os.access('C:/Users/ASUS/untitled2/kk', os.R_OK)


if __name__ == '__main__':
    mode1 = os.F_OK  # 测试path是否存在
    mode2 = os.R_OK  # 测试path是否可读
    mode3 = os.W_OK  # 测试path是否可写
    mode4 = os.X_OK  # 测试path是否可执行
    path1 = '../book'
    path2 = '../kk'
    path3 = '../kk/kk.txt'
    testPath(path1, mode1)
    testPath(path2, mode1)
    res = requests.get('http://www.tycqxs.com/48_48093/20003815.html')
    soup = BeautifulSoup(res.content, 'html.parser')
    article = soup.find('div', id="content").text
    print(article)
    while not os.path.exists(path2):  # 判断文件夹是否存在
        os.makedirs(path2)  # 新建文件夹
    with open(path3, 'ab+') as f:  # 写入文件
        print('start')
        f.write('哈呼和噫'.encode('utf-8'))
        f.write(article.encode('utf-8'))
        f.close()
