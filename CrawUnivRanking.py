# -*- coding:utf-8 -*-
# Author：YJX

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    """Get the page's substance of UnivRanking from internet"""
    try:
        # get the info of url by get function
        r = requests.get(url, timeout=30)
        # error info
        r.raise_for_status()
        # change coded format
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    """提取网页内容中的信息到合适的数据结构（列表）"""
    """get the info of this page then put into a list"""
    soup = BeautifulSoup(html, "html.parser")
    # find all child tag of tbody
    for tr in soup.find('tbody').children:
        # isinstance函数检测tr类型，如果不是标签类型则返回false
        if isinstance(tr, bs4.element.Tag):
            # 将一个tr标签中所有的td标签存为列表类型
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string, tds[6].string])
            # print(tds[1].string)

def printUnivList(ulist, num):
    """利用数据结构展示并输出结果"""
    # print the table name,{3}表示使用format函数的3号字符,即中文空格进行填充
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校", "总分", "科研规模", chr(12288)))
    saveToTxt("排名"+'\t'+"学校"+'\t'+"总分"+'\t'+"科研规模"+'\n\n')
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
        saveToTxt(u[0]+'\t'+ u[1]+'\t'+ u[2]+'\t'+u[3]+'\t'+ '\n\n')
    # The para num is the number of the reuslt that you want print in console.
    print("Suc"+str(num))

def saveToTxt(str):
    """save results to txt file"""
    f = open("E:\学习课件\Python网络爬虫与信息提取\DataFiles\高校排名(3).txt", 'a')
    f.write(str)
    f.close()

def main():
    """Main function of this project"""
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    # Put substance of html into uinfo
    fillUnivList(uinfo, html)
    # print the information of university ranking
    printUnivList(uinfo, 20)

main()
