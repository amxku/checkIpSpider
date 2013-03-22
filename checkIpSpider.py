#!/usr/bin/env python
# -*- coding:utf-8 -*-
# check ip is spider / amxku@sebug.net  / 2012-03-22 / v0.1
#
import time,re
from subprocess import Popen,PIPE
from threadpool import ThreadPool

def checkIpNslookup(arg):
    cmd = 'nslookup %s' % arg.strip()
    handle = Popen(cmd, stdout = PIPE, stderr = PIPE, shell = True).stdout
    re_handle = handle.read()
    handle.close()

    # name 关键词
    botkey = ['baidu','google','yahoo','msn']

    if re.search('name',re_handle.lower()):
        for bk in botkey:
            checkkey = re.search(bk,re_handle)
            if checkkey:
                print "%s-%s\n" % (arg.strip(),bk)
                break

if __name__ == "__main__":
    starttime = time.time()
    ipfiles = open('ip_list.txt','r')
    # 开始线程操作
    tp = ThreadPool(500)
    for cip in ipfiles.xreadlines():
        tp.push(checkIpNslookup, cip)
    tp.wait()
    print tp.busy()
    print 'done ,used :%s' % str(time.time()  - starttime)

