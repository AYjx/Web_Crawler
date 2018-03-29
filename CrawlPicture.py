# -*- coding:utf-8 -*-
# Author：YJX

import requests
import os

url = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1096328880,3118396530&fm=27&gp=0.jpg"
root = "E://Craw//pictures//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        '''判断根目录是否存在，目录不存在，则建立'''
        os.mkdir(root)
    if not os.path.exists(path):
        '''判断文件是否存在'''
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
