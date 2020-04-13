# -*- coding: utf-8 -*-
import log
import dirscan_burst
import yundama
import click
import vul_scan
import door_scan
import run_exp
import threading
import queue
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()
import os
#os.popen('export LC_ALL=C.UTF-8 && export LANG=C.UTF-8')

@click.command()
@click.option('--cmd',default='scan',type=str,help='操作指令')
@click.option('--url',type=str,help='目标url')
@click.option('-t',default=50,type=int,help='线程数')
@click.option('--dir',default='/var/log/',type=str,help='日志路径')
@click.option('--user',default='admin',type=str,help='用户名或字典路径')
@click.option('--password',default='password',type=str,help='用户密码或字典名')
@click.option('--file',default='password',type=str,help='目录扫描字典名')
@click.option('--target_url',default='password',type=str,help='用户登录界面url')
@click.option('--target_post',default='password',type=str,help='用户密码提交url')
@click.option('--target_captcha',default='password',type=str,help='验证码url')

def manage(cmd,url,t,dir,user,password,file,target_url,target_post,target_captcha):
    pool = Pool(t)
    if cmd == "log":
        win = log.Win(dir,t)
        win.deal()
    elif cmd == "door_scan":
        local_door =  door_scan.Local_door(dir)
        local_door.content_scan()
    elif cmd == "burst":
        dirscan_burst.explode(target_url,target_post,user,password)
    elif cmd == "yundama":
        yundama.yundama(target_url,target_post,target_captcha,password)
    elif cmd == "scan":
        vul_scan.vul_scan(url)
    elif cmd == "exp":
        run_exp.run_exp(url)
    else:
        help = """
        '--cmd',default='scan',type=str,help='操作指令'
        '--url',type=str,help='目标url'
        '-t',default=50,type=int,help='线程数'
        '--dir',default='/var/log/',type=str,help='日志路径'
        '--user',default='admin',type=str,help='用户名或字典路径'
        '--password',default='password',type=str,help='用户密码或字典名'
        '--file',default='password',type=str,help='目录扫描字典名'
        '--target_url',default='password',type=str,help='用户登录界面url'
        '--target_post',default='password',type=str,help='用户密码提交url'
        '--target_captcha',default='password',type=str,help='验证码url'
        """
        print(help)


if __name__ == '__main__':
    manage()

