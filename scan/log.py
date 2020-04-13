#coding: utf-8

import threading
import queue
import logdeal
import os

class Win(object):
    def __init__(self,dirname,t):
        self.dirname = dirname
        self.t = t
        #self.rules = rules

    def all_path(self):
        result = []
        for maindir, subdir, filenamelist in os.walk(self.dirname):
            for filename in filenamelist:
                if ".txt" in filename or ".log" in filename:
                    path = (maindir + "\\" + filename)
                    result.append(path)
        return result

    #paths = all_path(("D:\实习\毕业设计\demo").decode('utf-8').encode('gbk'))
    def deal(self):
        paths = self.all_path()
        for path in paths:
            path = str(path)
            # print(path)
            filename = path
            #thread = 10
            logdeal.analysislog(filename,self.t)
            #file = open(filename.decode('utf-8'), 'rb')
            #for line in file:
                #print(line.strip())

class Linux(object):
    def __init__(self):
        pass



# dirname = ("D:\实习\毕业设计\scan\demo")
# win = Win(dirname,3)
#
# win.deal()