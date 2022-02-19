Email=""
FofaKey=""

#email与fofakey获取规则：
#fofa首页随便输入关键词点击查找
#然后点击api 看url中的email与key
#https://fofa.info/api/v1/search/all?email=&key=

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55",
    "Referer": "https://api.fofa.info/",
    "Cookie": ""
}

#headers必须设置cookie
#不然无法获取页码