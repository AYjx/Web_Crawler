#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html)

namelist = bs0bj.findAll("span", {"class":"green"})
for name in namelist:
    print(name.get_text())
