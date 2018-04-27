# 找 robots.txt
import requests

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}  # 代理
link = 'https://%s/robots.txt'  # https
start = input("请输入要读取‘robots.txt’的网址：")
res = requests.get(link % start, proxies=proxies)
print(res.text)
