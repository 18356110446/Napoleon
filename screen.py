import requests
import re
import time
import random

i = 0
k = 0

for i in range(2, 9):
    url = f'https://wallhaven.cc/toplist?page={i}'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
    res = requests.get(url=url, headers=header)
    print(f'第{i}开始下载')
    pic = re.findall('<a class=.*? href=\"(.*?)\" ', res.text)
    # print(pic)
    print(f'第{i}网址截取成功')
    for a in range(7, 16):
        k += 1
        spic = requests.get(url=pic[a], headers=header)
        rpic = re.findall('<img id=".*?" src="(.*?)" alt=\".*?\" data-wallpaper-id=".*?\" ', spic.text)[0]
        # print(rpic)
        print(f'{i}-{k}网页截取成功')
        picture = requests.get(url=rpic, headers=header)
        print(f'{i}-{k}照片下载成功')
        with open(f'D:/wallpaper/{i}-{k}.jpg', 'wb+') as x:
            x.write(picture.content)
            # with open(f'{k}.jpg','wb+') as x:
            #     x.write(picture.content)
            print(f'{i}-{k}以成功下载')
        time.sleep(random.random() * 3)
        print('进入下一张照片……')
