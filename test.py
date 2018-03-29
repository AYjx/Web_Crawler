# -*- coding:utf-8 -*-
# Author：YJX

from bs4 import BeautifulSoup
import time
import requests
import os
import csv



headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}

if __name__ == '__main__':
    num = []
    urls = ['class/{}.html'.format(num[i]) for i in range(0, 4)]
    list = []
    for url in urls:
        wb_data = requests.get(url, headers)
        soup = BeautifulSoup(wb_data.text, 'html.parser')
        imgs = soup.select('img')
        print(len(imgs))
        for img in imgs:
            # 单个img中包含多个链接（全一样）
            print(img)
            # 获取img中名为src 的字符串(链接)
            photo = img.get('src')
            print(photo)
            # list.append(photo)
            root = 'F:/DataFiles/Pictures/'
            if not os.path.exists(root):
                '''判断根目录是否存在，目录不存在，则建立'''
                os.mkdir(root)
            # for item in list:
            # path = root + list[-1].split('?')[0][-10:]
            path = root + photo[-20:]
            # print(list[-1])
            i = 1
            while os.path.exists(path):
                '''如果文件存在，则修改保存路径'''
                path = root + ""+str(i)+"_" + photo.split('?')[0][-10:]
                i += 1
            data = requests.get(photo, headers)
            with open(path, 'wb') as f:
                f.write(data.content)
                f.close()
            time.sleep(2)
                # print("文件保存成功")