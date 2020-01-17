# coding: utf-8
from package import *
import json
import codecs
import threading
import time
# content = http({
#     'url':'http://192.168.1.118/headset/Public/Home/Images/logo1/zx2.jpg',
#     'type':'post',
#     'data':{'asd':123,'re':22}
# })
# print(content.text)
# print(content.raw.read())
# print(content.headers)
# content.status_code #响应状态码
# content.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# content.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# content.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# content.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# #*特殊方法*#
# content.json() #Requests中内置的JSON解码器
# content.raise_for_status() #失败请求(非200响应)抛出异常

# savefile({
#     'url':'http://127.0.0.1/admin','addr':'C:\\Users\Administrator\Desktop/1.jpg'
# })

# post({
#     'url':'http://192.168.1.118/headset/Public/Home/Images/logo1/zx2.jpg',
#     'end':'utf-8',
#     'data':{},
#     'header':{}
# })

# get({
#     'url':'http://192.168.1.118/headset/Public/Home/Images/logo1/zx2.jpg',
#     'end':'utf-8',
#     'header':{}
# })
# savefile({
#     'url':'https://yl-x.cn',
#     'addr':'C:\\Users\Administrator\Desktop/1.html'
# })
# asd = http({
#     'url':'http://127.0.0.1/ylx/Uploads/files_cp/2019-01-23/t15482132601921681169.png',
#     'end':'utf8'
# }).text
# # print(asd)
# f = codecs.open(r'C:\\Users\Administrator\Desktop/1.jpg', 'wb')

# f.write(asd) 

# asd.flush()

# asd.close()
# print(get({
#     'url':"https://yl-x.cn"
# }))
# saveImg({
#     'url':'http://127.0.0.1/ylx/Uploads/files_cp/2019-01-23/t15482132601921681169.png',
#     'addr':'C:\\Users\Administrator\Desktop/1123'
# })
# list = []
# list2 = ['1','2','3','3']
# heavy(list,list2)
# print(list)
# print(list2)


# a = 0
# def fuc():
#     global a
#     a += 1
#     print(a)
#     if(a>10):
#         print(t)
#         return False
# t = setT(1,fuc)

#threadName.exit()退出线程
# def goo(data):
#   print(data.name)
#   pass
# class myThread (threading.Thread):
#     def __init__(self,name,counter = goo):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.func = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         self.func(self)
#         print ("退出线程：" + self.name)
# 创建新线程
# thread1 = myThread("Thread-1")
# thread2 = myThread("Thread-2")
# thread3 = myThread("Thread-3")
# print(threading.currentThread() ,1223)
# # 开启新线程
# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()
# print ("退出主线程")
# print('122312')
# savefile({
#     'url':'https://yl-x.cn',
#     'addr':'C:\\Users\Admin\Desktop/demo/1.html'
# })

