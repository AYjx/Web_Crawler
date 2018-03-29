# -*- coding:utf-8 -*-
# Author：YJX

import requests
import re

def getHTMLText(url):
    """Get the page's substance of taobao from internet"""
    try:
        r = requests.get(url, timeout = 300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    """解析页面，ilt是结果的列表类型,使用正则表达式来实现对商品价格和名字的获取"""
    try:
        # list类型,获得所有价格信息，用反斜杠表示引入双引号（源代码中键和值都有双引号）
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        # 获取所有商品名字， *?表示最小匹配
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        # 匹配价格和商品名
        for i in range(len(plt)):
            # 使用冒号分割字符串
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    """输出商品列表"""
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count+1
        print(tplt.format(count, g[0], g[1]))

def saveToTxt(str):
    """save results to txt file"""
    f = open("E:\学习课件\Python网络爬虫与信息提取\DataFiles\淘宝商品-书包(2).txt", 'a')
    f.write(str)
    f.close()

def main():
    """Main function of this project"""
    goods = '书包'
    # 爬取深度
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    # 输出结果的列表
    infoList = []
    # 使用for循环对每一个页面进行处理
    for i in range(depth):
        try:
            # 每个页面的URL链接
            url = start_url + '' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()
