import threading
def fun():
    pass
def setT(a,func = fun):
    global tss
    typ = func()
    if(typ == False):
        tss.cancel()
        return
    tss = threading.Timer(a, setT,(a,func))
    tss.start()
    return tss

