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
        'Cookie': '__cfduid=d467492569e830ce63f5c2f75d9357ad91601482105; G_ENABLED_IDPS=google; G_AUTHUSER_H=0',
        'token' : '5f748d95c6eb4d13ef1f0295.2lxogp1qJy1633018128351.108280135267653011049'
        }
        
data = {
        # action : hunt2, train2, eat2, girl2, good2, sit2, fish2
        'action':'good2',
        }
# u is yours
url = 'https://mykirito.com/api/my-kirito/doaction?u=5f748d95c6eb4d13ef1f0295'
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