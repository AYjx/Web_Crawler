#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

import requests
from bs4 import BeautifulSoup
import bs4
import traceback
import re
"""
蚂蜂窝（静态）网页爬取，
获取用户名、评论的景点名、评分、时间、评论，
并保存在txt文件
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

def fillReList(spotList, scoreList, reviewList,timeList, html):
    """获取用户的评论信息，包括用户名、景点、评分、评论"""
    soup = BeautifulSoup(html, "html.parser")
    userName = soup.find('span', 'MAvaName').get_text()
    print("用户名：", userName)
    spots = soup.find_all('h3', 'title')
    scores = soup.find_all('span', 'tip')
    reviews = soup.find_all('div', 'poi-rev _j_comment')
    times = soup.find_all('span', 'time')
    if spots==None:
        print("此页面不包含景点！")
        return ""
    else:
        for spotname in spots:
            spotList.append(spotname.get_text())
        for score in scores:
            scoreList.append(score.get_text())
        for review in reviews:
            reviewList.append(review.get_text())
        for time in times:
            timeList.append(time.get_text())
        return userName




def printInfoList(spotList, scoreList, reviewList, timeList, uName):
    """print all infomation"""
    openTxt("用户名：" + uName + '\n\n' + "编号" + '\t' + "景点" + '\t' + "评分" + '\t' + "评论" + "时间" + '\n\n', uName)
    # saveToTxt("用户名：" + uName + '\n', uName)
    tplt = "{0:^10}\t{1:{5}^10}\t{2:{5}^10}\t{3:{5}^10}\t{4:^10}"

    for i in range(len(spotList)):
        print(tplt.format(i, spotList[i], scoreList[i], timeList[i], reviewList[i], chr(12288)))
        saveToTxt(str(i) + '\t' + spotList[i]+'\t' + scoreList[i]+'\t' + timeList[i] + '\t' + reviewList[i] + '\n', uName)


def openTxt(str, Nstr):
    """save results to txt file"""
    f = open("G:\学习课件\Python网络爬虫与信息提取\DataFiles\蚂蜂窝(1" + Nstr + ").txt", 'w', encoding='utf-8')
    f.write(str)
    f.close()


def saveToTxt(str, Nstr):
    """save results to txt file"""
    f = open("G:\学习课件\Python网络爬虫与信息提取\DataFiles\蚂蜂窝(1" + Nstr + ").txt", 'a', encoding='utf-8')
    f.write(str)
    f.close()


def main():
    """Main function of this project"""
    url = 'http://www.mafengwo.cn/u/lalafc/review.html'
    spotList = []
    scoreList = []
    reviewList = []
    timeList = []
    uName = ""
    html = getHTMLText(url)
    if html==None:
        print("空白页面")
    else:
        uName = fillReList(spotList, scoreList, reviewList, timeList, html)
        printInfoList(spotList, scoreList, reviewList, timeList, uName)




main()