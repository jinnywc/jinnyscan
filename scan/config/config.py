#coding:utf-8

ceye_dns = ""       #ceye的dns解析记录
ceye_http = ""     #ceye的http解析记录
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}                                #设置的默认代理，便于抓包

apiurl = 'http://api.yundama.com/api.php'          #云打码api的url
username    = ''                             #自己云打码平台的账户
password    = ''                             #自己云打码平台的密码
appid       =  7289                                #自己云打码平台的appid
appkey      = ''   #自己云打码平台的appkey
filename    = '1.jpg'                              #验证码下载到本地的文件名
codetype    = 1004                                 #验证码的类型
timeout     = 60                                   #设置的延时

username_tag = "username"                          #爆破时的用户参数
password_tag = "password"                          #爆破时的密码参数

filename_log = "./rules/door_rules.txt"            #日志分析的规则库文件

host = "127.0.0.1"                                 #数据库host
user = "root"                                      #用户
passwd = "root"                                    #密码
dbname = "demo"                                    #数据库

cookie = ""                                        #设置的cookie