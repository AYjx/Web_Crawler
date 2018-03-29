# -*- coding:utf-8 -*-
# Author：YJX

import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code="utf-8"):
    """ 获得URL对应的页面"""
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    """获得股票列表，参数lst存储所有股票信息，参数stockURL获得股票列表的URL网站"""
    html = getHTMLText(stockURL, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    # 找到所有a标签
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    """获得每一支个股的信息"""
    count = 0
    for stock in lst:
        """从lst中获取每个个股的编号，链接由主体加编号加html组成"""
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            # 判断页面是否为空
            if html == "":
                continue
            # 字典中存放返回的所有个股信息
            infoDict = {}
            # 解析网页
            soup = BeautifulSoup(html, 'html.parser')
            # 源代码中，所有的股票信息封装在div标签下，属性是stock-bets；所以，搜索标签，找到个股信息
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            # 在标签的属性bets-name下查找 股票名称
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            # 将信息增加到字典中
            infoDict.update({'股票名称':name.text.split()[0]})
            # 源代码中标签dt下存键，dd下存值，获取键值对
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            # 将股票信息还原成键值对，存到字典中
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                print("\r当前进度:{:.2f}%".format(count*100/len(lst)), end="")
        except:
            # 获得错误信息
            count = count+1
            print("\r当前进度:{:.2f}%".format(count * 100 / len(lst)), end="")
            # traceback.print_exc()
            continue

def main():
    """Main function of this project"""
    # 获得股票列表的链接
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    # 获得股票信息链接的主体
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    # 文件保存地址
    output_file = 'E:\学习课件\Python网络爬虫与信息提取\DataFiles\BaiDuStockInfo.txt'
    # 股票信息
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()