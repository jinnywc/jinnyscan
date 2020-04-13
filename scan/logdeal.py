# -*- coding: utf-8 -*-
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()
import re
import os
import click
from urllib.parse import unquote

#os.popen('export LC_ALL=C.UTF-8 && export LANG=C.UTF-8')

rules = {
    'Scanner': {
        'scanner': r'SCANNER TEST_RULE',
    },
    'Login': {
        'login': r'(login|Login)',
    },
    'SQLinject': {
        'sql': r'(SQLI|SQLi)',
    },
    'ArbitraryFileOperation': {
        '任意文件upload': r'(upload|Upload)',
        '任意文件download': r'(download|Download)',
    },
    'dirtraversal': {
        'windows路径穿越': r'(win.ini|system.ini|boot.ini|cmd.exe|global.asa)',
        'linux路径穿越': r'(etc.*passwd|etc.*shadow|etc.*hosts|.htaccess|.bash_history)',
    },
    'CommandExecution': {
        '命令执行': r'(OS_COMMAND|CODE)',
    },
    'struts2vuln': {
        'struts005~009': r'xwork.MethodAccessor.denyMethodExecution',
        'struts013': r'_memberAccess.*ServletActionContext',
        'struts016': r'redirect:.*context.get',
        'struts019': r'xwork2.dispatcher.HttpServletRequest',
        'struts032~057': r'@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS',
    },
    'XSS': {
        'xss': r'XSS',
    },
    'SSTI': {
        '一般型': r'{{.*}}',
        'Ruby模板注入': r'<%.*%>',
        'Java模板注入': r'\${.*}',
    },
    'LDAP': {
        '一般型': r'\*[\(\)|]+',
    },
    'XXE': {
        '外部实体注入': r'(<\?xml.*\?>|<!.*>|<xsl.*>)',
    },
    'DangerRequests': {
        '不安全http方法': r'("put.*http/1.|"options.*http/1.|"delete.*http/1.|"move.*http/1.|"trace.*http/1.|"copy.*http/1.|"connect.*http/1.|"propfind.*http/1.)',
        '爬虫UA': r'(python-requests|python-urllib|"curl/)',
    }
}
# f = open('./result.txt', 'w+')
scanner = 0
sql = 0
xss = 0
fileop = 0
login = 0
rce = 0
other = 0


def analysisattack(log):
    # print(1)
    global scanner, sql, xss, fileop, login, rce, other
    if log:
        for key, value in rules.items():
            for key2, value2 in value.items():
                try:
                    match = re.search(value2, log, re.I)
                    # print(key)
                    if match:
                        # f.write('[*]日志: {0}\n'.format(log))
                        res = '[!]漏洞类型: {0}\t漏洞细节: {1}\t匹配规则: {2}'.format(key, key2, value2)
                        # print(u'{0}'.format(res))
                        # f.write('{0}\n\n'.format(res))
                        if key == 'Scanner':
                            scanner = scanner + 1
                        elif key == 'SQLinject':
                            sql = sql + 1
                        elif key == 'XSS':
                            xss = xss + 1
                        elif key == 'ArbitraryFileOperation':
                            fileop = fileop + 1
                        elif key == 'Login':
                            login = login + 1
                        elif key == 'truts2vuln' or key == 'SSTI' or key == 'ArbitraryCodeExcute':
                            rce = rce + 1
                        elif key == 'dirtraversal' or key == 'LDAP' or key == 'XXE' or key == 'DangerRequests':
                            other = other + 1


                except:
                    print(u'[-] 日志分析失败: {0}'.format(log))


def analysislog(f, t):
    global scanner, sql, xss, fileop, login, rce, other
    filename = f
    pool = Pool(t)
    logs = list()
    pat = list()
    patt = 'http.+\.cn'
    with open(filename, 'r') as fp:
        for line in fp:
            logs.append(line.strip())
            #print(line.strip())
    totalcount = len(logs)
    print(u'[*] 当前文件名: {0}'.format(f))
    print(u'日志数: {0}'.format(totalcount))
    pool.map(analysisattack, logs)
    #print("结果保存在同目录下的result.txt,每次保存会重置这个文件")
    res = '非法探测次数: {0}\t\r\n注入攻击次数: {1}\t\r\n跨站攻击次数: {2}\t\r\n任意文件上传/下载次数: {3}\t\r\n登录爆破次数: {4}\t\r\n远程命令执行次数: {5}\t\r\n其他攻击次数: {6}'.format(
        scanner, sql, xss, fileop, login, rce, other)
    print(res)
    scanner = 0
    sql = 0
    xss = 0
    fileop = 0
    login = 0
    rce = 0
    other = 0

#analysislog("D:\实习\毕业设计\demo\demo.txt",10)


