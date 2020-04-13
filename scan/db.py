#coding:utf-8
import pymysql
import sys
sys.path.insert(0,'.')
from config import config

'''
把爆破和漏洞扫描结果存入数据库
'''
host = config.host
user = config.user
passwd = config.passwd
dbname = config.dbname

class DB(object):
    def __init__(self,url,name,password):
        self.url = url
        self.name = name
        self.password = password
    def burstdb(self):
        con = pymysql.connect(host, user, passwd, dbname, charset='utf8')
        cursor = con.cursor()
        #url = "47.106.8.213"
        #name = "admin"
        #password = "password"
        sql = """INSERT INTO demo(url,name,password) VALUES ("%s","%s","%s")""" % (self.url, self.name, self.password)
        #print(sql)
        #sql1 = "SELECT * from demo" #测试语句
        cursor.execute(sql)
        #cursor.execute(sql1) #调试用
        datas = cursor.fetchall()
        #for data in datas:
            #print(list(data))
        con.commit()
        con.close()


#url = "127.0.0.2"
#name = "admin"
#password = "admin"
#db = DB(url,name,password)
#db.burstdb()

