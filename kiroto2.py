import requests
import json
import random
from time import sleep
headers= {
        'Host': 'mykirito.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
        'Accept': 'application/json, text/plain, /',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/json;charset=utf-8',
        'Content-Length': '18',
        'Origin': 'https://mykirito.com',
        'Connection': 'close',
        'Referer': 'https://mykirito.com/',
        # Cookie is yours
        'Cookie': '__cfduid=d0bea3e426eea6df599ae7b17f8db97431601481844; G_ENABLED_IDPS=google; G_AUTHUSER_H=0',
        'token' : '5f748e420ed95f13e37cf4da.g2AaLRdzuG1633017848766.105621689573580379135'
        }
        
data = {
        # action : hunt2, train2, eat2, girl2, good2, sit2, fish2
        'action':'girl2',
        }
# u is yours
url = 'https://mykirito.com/api/my-kirito/doaction?u=5f748e420ed95f13e37cf4da'
count = 0

# for i in range(28800):
#     sleep(1)
#     print("經過了{sec}秒啦 JOJO".format(sec=i))

while True:
    r = requests.post(url, headers = headers, json=data)
    count+=1
    print(count, r.text)
    s = random.randint(66, 75)
    sleep(s)