# jinnyscan
一款轻量型的综合扫描器

扫描器使用的是python3环境
在使用前需要配置config目录下的config.py
扫描器的主程序是mian.py

扫描器有五个功能：爆破，本地日志分析，后门检测，漏洞扫描和目录扫描
在爆破时db.py可以把爆破的结果存入数据库,sql.sql为创建数据库表的文件，demo.php文件可以使放到web目录，访问可以得到爆破的结果

爆破
python36 main.py --cmd burst --user admin --password pass.txt --target_url 登录界面的url --target_post 用户密码提交到的url

云打码爆破

python36 main.py --cmd yundama --target_url 用户登录界面的url --target_post 用户密码及图片验证码提交到的url --target_captcha 图片验证码生成的url --password pass.txt

常规漏洞扫描

python36 main.py --url 目标url --cmd scan

exp漏洞扫描

python36 main.py --cmd exp --url 目标url

本地日志分析

python36 main.py --cmd log --dir 需要日志分析的目录 -t 线程数

后门检测

python36 main.py --cmd door_scan --dir 需要后门检测的目录

可以使用命令获取程序的帮助信息：python3 mian.py --help  

