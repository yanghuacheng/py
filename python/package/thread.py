import threading
import time
def goo(data,query = []):
    print(122222222223)
    pass
class myThread (threading.Thread):
    def __init__(self,name,counter = goo,query = []):
        threading.Thread.__init__(self)
        self.name = name
        self.func = counter
        self.query = query
    def run(self):
        print ("开始线程：" + self.name)
        threadLock.acquire()
        self.func(self)
        threadLock.release()
        print ("退出线程：" + self.name)
threadLock = threading.Lock()
threads = []
# 创建新线程
# thread1 = myThread("Thread-1")
# thread2 = myThread("Thread-2")