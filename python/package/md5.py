import hashlib
def getmd5(filename):
    m = hashlib.md5()
    m.update(filename.encode('utf-8'))
    md5_value = m.hexdigest()
    return md5_value

# 爬虫url去重
def heavy(list,list2 = []):
    newlst = []
    for x in list2:
        md = getmd5(x)
        if(md in list):
            pass
        else:
            list.append(md)
            newlst.append(x)
    return newlst