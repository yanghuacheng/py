#coding=utf-8
import requests
import json
import os
import urllib.request
import ssl
import imghdr
# http请求｛url:请求地址，end：响应编码，data：请求参数，header：请求头参数，type：请求方式（get，post），cookie：请求头cookies｝
def http(obj):
    ver = True
    if(('url' in obj) == False):
        return '请填写url地址' 
    if(obj['url'].find('https') == 0):
        ver = False
    if(('header' in obj) == False):
        obj['header'] = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    if(('data' in obj) == False):
        obj['data'] = {}
    if(('cookie' in obj) == False):
        obj['cookie'] = {}    
    if(('type' in obj) == False):
        obj['type'] = 'get'
    if(obj['type'] == 'get'):
        r = requests.get(obj['url'],headers = obj['header'],params = obj['data'],cookies = obj['cookie'],verify=ver)
    elif(obj['type'] == 'post'):
        r = requests.post(obj['url'],headers = obj['header'],params = json.dumps(obj['data']),cookies = obj['cookie'],verify=ver)
    if('end' in obj):
        r.encoding = obj['end']
    else:
        r.encoding = 'utf-8'
    return r
# get请求｛url:请求地址，end：响应编码，header：请求头参数｝
def get(obj):
    if(('end' in obj) == False):
        obj['end'] = 'utf-8'
    if(('url' in obj) == False):
        return
    if(obj['url'].find('https') == 0):
        ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    req = urllib.request.Request(url=obj['url'], headers=headers)
    res = urllib.request.urlopen(req)
    page_source = res.read().decode(obj['end'])
    return page_source
# post请求｛url:请求地址，end：响应编码，data：请求参数，header：请求头参数｝
def post(obj):
    if(('end' in obj) == False):
        obj['end'] = 'utf-8'
    if(('url' in obj) == False):
        return
    if(('data' in obj) == False):
        obj['data'] = {}
    if(obj['url'].find('https') == 0):
        ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    postdata = urllib.parse.urlencode(obj['data']).encode('utf-8')
    req = urllib.request.Request(url=obj['url'], data=postdata, headers=headers)
    res = urllib.request.urlopen(req)
    page_source = res.read().decode(obj['end'])
    return page_source

# 请求文件并保存
# obj(｛url：请求文件地址，addr：保存地址｝)
def fun(a,b,c):
    # os.system('cls')
    per=100*a*b/c
    per=round(per, 2)
    if(per>100):
        per=100
    # print(per)
def savefile(obj,func = fun):
    if(('url' in obj) == False):
        return
    if(obj['url'].find('https') == 0):
        ssl._create_default_https_context = ssl._create_unverified_context
    if(('addr' in obj) == False):
        return 'addr保存地址不能为空'
    urllib.request.urlretrieve(obj['url'],obj['addr'],func)

def saveImg(obj,func = fun):
    data = http(obj).content
    s=imghdr.what(None,data)
    if(s == None):
        return '请求内容不是图片'
    f = open(obj['addr'] + '.' + s,'ab')   
    with f as f:
        f.write(data)
        f.close()
    return s
    
        
    
    
