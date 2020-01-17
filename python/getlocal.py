from package import *
from bs4 import BeautifulSoup
import os
import time
yum = '127.0.0.1'
htpUrl = 'http://127.0.0.1'

addr = 'C:\\Users\Admin\Desktop\wangzhan'
addrcs = addr + '/css'
addrjs = addr + '/js'
addrimg = addr + '/img'
def getlink(dom,str=''):
    return dom.get(str)
def getsave(lst,dirname,name,repl):
    for ia in lst:
        lkl = getlink(ia,name)
        if(lkl != None):
            lsss = lkl
            if(len(lkl[0]) > 0):
                if(lkl[0] == '/'):
                    pass
                else:
                    lkl = '/' + lkl
            filename = getmd5(lkl)
            linkpath = dirname + '/' + filename
            if(dirname != 'img'):
                addrss = os.path.exists(addr + '/' + linkpath + '.' + dirname)
                if(addrss == False):
                    # # print(htpUrl + lkl)
                    # print(lkl + 'img')
                    # # print(addr + '/' + linkpath + '.' + dirname)
                    # print('错误前')
                    try:
                        savefile({'url':htpUrl + lkl,'addr':addr + '/' + linkpath + '.' + dirname})
                    except:
                        pass
                repl = repl.replace(lsss,'./' + linkpath+ '.' + dirname)
            else:
                try:
                    tys = saveImg({'url':htpUrl + '/' + lkl,'addr':addr + '/' + linkpath})
                    repl = repl.replace(lsss,'./' + linkpath + '.' + tys)
                except:
                    pass
    return repl
list0 = []

def Thre(data):
    goto(data.query[0])

def goto(url = ''):
    heavy(list0,url)  
    print(url + '开始')
    rmname = getmd5(url)
    data = http({'url':url,'end':'utf-8'}).text
    dom = BeautifulSoup(data,'html.parser')
    
    img_list = dom.findAll('img')
    data = getsave(img_list,'img','src',data)
    print(url + '页面图片采集完成')

    css_list = dom.findAll('link')
    data = getsave(css_list,'css','href',data)
    print(url + '页面css采集完成')

    js_list = dom.findAll('script')
    data = getsave(js_list,'js','src',data)
    print(url + '页面js采集完成')
    
    
    lls = addr + '/' +rmname + '.html'
    a_list = dom.findAll('a')
    for htm in a_list:
        if(htm.get('href') != None and htm.get('href') != '' and htm.get('href')[0] != '#'):
            if(len(htm.get('href')) > 0):
                if(yum in htm.get('href') or htm.get('href')[0:4] != 'http'):
                    if(htm.get('href')[0] == '/'):
                        alink = htpUrl + htm.get('href')
                    else:
                        alink = htpUrl + '/' + htm.get('href')
                    data = data.replace('href="' + htm.get('href') + '"','href="' + addr + '/' + getmd5(alink) + '.html"')
    if(os.path.exists(lls) == True):
        os.remove(lls)
    f = open(lls,'w',-1,'utf-8')   
   
    with f as f:
        f.write(data)
        f.close()
    print(url + '页面写入完成')

    list1 = []
    for a in a_list:
        if(a.get('href') != None and a.get('href') != '' and a.get('href')[0] != '#'):
            if(len(a.get('href')) > 0):
                if(yum in a.get('href')  or a.get('href')[0:4] != 'http'):
                    if(a.get('href')[0] == '/'):
                        adlk = htpUrl + a.get('href')
                    else:
                        adlk = htpUrl + '/' + a.get('href')
                    list1.append(adlk)
    list1 = heavy(list0,list1)  
    print(url + '准备爬取页面链接') 
    # for com in list1:
    #     print(com)
    #     # return
    #     time.sleep(2)
    #     myThread(getmd5(com),Thre,[com]).start()
def mains():
    addrs = os.path.exists(addr)
    if(addrs == False):
        os.mkdir(addr)
		
    addrs = os.path.exists(addrcs)
    if(addrs == False):
        os.mkdir(addrcs)
    addrs = os.path.exists(addrjs)
    if(addrs == False):
        os.mkdir(addrjs)
    addrs = os.path.exists(addrimg)
    if(addrs == False):
        os.mkdir(addrimg)
    goto(htpUrl + '/yyy')
mains()