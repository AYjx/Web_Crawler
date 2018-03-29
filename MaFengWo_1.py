#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

import requests
from bs4 import BeautifulSoup
import bs4
import traceback
import re
"""
蚂蜂窝（静态）网页爬取，获取用户名和评论的景点名
"""
def getHTMLText(url, code="utf-8"):
    """ 获得URL对应的页面"""
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""

def fillReList(html):
    nList = []
    soup = BeautifulSoup(html, "html.parser")
    userName = soup.find('span', 'MAvaName').get_text()
    print("用户名：", userName)
    c = 0
    nList = soup.find_all('h3', 'title')
    if nList==None:
        print("此页面不包含景点！")
        return ""
    else:
        for spotname in nList:
            print(spotname.get_text())


# def printUnivList(nList):




def main():
    """Main function of this project"""
    url = 'http://www.mafengwo.cn/u/34019438/review.html'
    # uInfo = []
    html = getHTMLText(url)
    fillReList(html)



main()