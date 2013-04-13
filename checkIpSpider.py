#!/usr/bin/env python
# -*- coding:utf-8 -*-
# check ip is spider  /  amxku@sebug.net  /  2012-03-22 / v0.2
#
import time
import socket
from threadpool import ThreadPool


def getIpHostName(arg):
    try:
        botkey = ['baidu', 'google', 'yahoo', 'msn']
        handle = socket.gethostbyaddr(arg)[0]
        if any(x in handle for x in botkey):
            print "%s-%s\n" % (arg, handle.split('.')[-2])
    except socket.herror:
        pass

if __name__ == "__main__":
    starttime = time.time()
    ipfiles = open('ip_list.txt', 'r')
    # 开始线程操作
    tp = ThreadPool(10)
    for cip in ipfiles.xreadlines():
        tp.push(getIpHostName, cip.strip())
    tp.wait()
    ipfiles.close()
    print tp.busy()
    print 'done ,used :%s' % str(time.time() - starttime)
