import requests
from lxml import etree
import base64
import re
import time
import config
import json
from urllib.parse import quote,unquote

def spider():
    searchbs64 = quote(str(base64.b64encode(config.SearchKEY.encode()), encoding='utf-8'))
    print("爬取页面为:https://fofa.info/result?&qbase64=" + searchbs64)
    html = requests.get(url="https://fofa.info/result?&qbase64=" + searchbs64, headers=config.headers).text
    tree = etree.HTML(html)
    try:
        pagenum = tree.xpath('//li[@class="number"]/text()')[-1]
    except Exception as e:
        print(e)
        pagenum = '0'
        pass
    print("该关键字存在页码: "+pagenum)
    config.StartPage=input("请输入开始页码:")
    config.StopPage=input("请输入终止页码:")
    doc = open("ip.txt", "a+")
    ufile = open("url.txt", "a+")
    for i in range(int(config.StartPage),int(pagenum)):
        print("正在爬取第" + str(i) + "页")
        rep = requests.get('https://fofa.info/api/v1/search/all?email='+config.Email+'&key='+config.FofaKey+'&qbase64='+searchbs64+'&page='+str(i), headers=config.headers)
        list = json.loads(rep.text)
        if list["error"] == True and list["errmsg"] == "403 forbidden, please continue use page.":
            print("没有更多的url可以爬取了")
            break
        if list["error"] == True:
            print("发生致命错误，原因"+list["errmsg"])
            break
        if list["error"] != True:
            for item in list["results"]:
                print(item[1]+":"+item[2])
                doc.write(item[1]+":"+item[2]+"\n")
                ufile.write(item[0]+"\n")
        if i==int(config.StopPage):
            break
        time.sleep(config.TimeSleep)
    ufile.close()
    doc.close()
    print("爬取已完成，回车键结束程序。")
    input()

def main():
    logo()
    check()
    init()
    spider()

def logo():
    print('''
    FOFA.INFO Spider
    Made By Summer
    ''')

def check():
    if config.Email=="" or config.FofaKey=="":
        print("请配置config文件")
        input()
        exit(0)
    print("检测config成功")
    return

def init():
    config.TimeSleep = int(input('请输入爬取每一页等待的秒数:'))
    config.SearchKEY = input('请输入fofa搜索关键字:')
    return

if __name__ == '__main__':
    main()
