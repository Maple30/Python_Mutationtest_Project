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
        'Cookie': '__cfduid=d5132150997e45e04546f758b2eaae5ca1601173037; G_ENABLED_IDPS=google',
        'token' : '5f6ff64152107e22c72088e4.xBqojgs3VM1632709057014.113290161947104053967'
        }
        
        
data = {
        # action : hunt2, train2, eat2, girl2, good2, sit2, fish2
        'action':'hunt2',
        }
# u is yours
url = 'https://mykirito.com/api/my-kirito/doaction?u=5f6ff64152107e22c72088e4'
count = 0

while True:
    r = requests.post(url, headers = headers, json=data)
    count+=1
    print(count, r.text)
    s = random.randint(66, 75)
    sleep(s)