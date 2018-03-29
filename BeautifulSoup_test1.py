#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    """get the html title"""
    try:
        html=urlopen(url)
    except HTTPError as ex:
        return None
    try:
        bs0bj = BeautifulSoup(html.read())
        title = bs0bj.body.h1
    except AttributeError as ex:
        return None

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("未找到页名")
else:
    print(title)
