#!/usr/bin/env python
# -*- coding:utf-8 -*-
# check ip is spider / amxku@sebug.net  / 2012-03-22 / v0.2
#
import time,re,socket
from threadpool import ThreadPool

def getIpHostName(arg):
    try:
        handle = socket.gethostbyaddr(arg.strip())[0]
        #return any(x in socket.gethostbyaddr(arg.strip())[0] for x in ['baidu','google','yahoo','msn'])
        # name 关键词
        botkey = ['baidu','google','yahoo','msn']
        for bk in botkey:
            checkkey = re.search(bk,handle)
            if checkkey:
                print "%s-%s\n" % (arg.strip(),bk)
                break
    except socket.herror:
        pass

if __name__ == "__main__":
    starttime = time.time()
    ipfiles = open('ip_list.txt','r')
    # 开始线程操作
    tp = ThreadPool(10)
    for cip in ipfiles.xreadlines():
        tp.push(getIpHostName, cip)
    tp.wait()
    print tp.busy()
    print 'done ,used :%s' % str(time.time()  - starttime)