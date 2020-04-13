#coding:utf-8
import os
import re
import sys
sys.path.insert(0,'.')
from config import config

rules = {
    "webshell":{
        'phpwebshell':r'(eval|assert|preg_replace|create_function|array_map|call_user_func|call_user_func_array)',
        'aspwebshell':r'(request|eval|Request.Item|execute)',
        'jspwebshell':r'(request.getParameter|Runtime.getRuntime|excuteCmd)',
    },
    "反弹shell":{
        'php反弹shell':r'(system|exec|passthru|shell_exec)',
        'asp反弹shell':r'(WScript.CreateObject("WScript.Shell")|server.createobject("wscript.shell").exec)',
        'jsp反弹shell':r'(Runtime.getRuntime)',
    }
}
name_rules = list()
filename = config.filename_log
with open(filename,'r') as fp:
    for line in fp:
        name_rules.append(line.strip())


class Local_door():
    def __init__(self,dirname):
        self.dirname = dirname
    def filename_scan(self):
        paths = list()
        for maindir, subdir, filenamelist in os.walk(self.dirname):
            for filename in filenamelist:
                path = (maindir + "\\" + filename)
                paths.append(path)
                name = filename.split(".",1)[0]
                if name_rules.count(name):
                    print("发现可疑文件：" + path)
        return paths
    def content_scan(self):
        paths = self.filename_scan()
        for path in paths:
            i = 0
            content = list()
            with open(path,'rb') as fp:
                for line in fp:
                    content.append(line.strip())
            for key1,value1 in rules.items():
                for key2,value2 in value1.items():
                    for line in content:
                        line = str(line)
                        result = re.search(value2, line)
                        if result:
                            if ".php" in path:
                                print(path + "文件发现疑是：phpwebshell")
                                i = i + 1
                                break
                            elif ".asp" in path:
                                print(path + "文件发现疑是：aspwebshell")
                                i = i + 1
                                break
                            elif ".jsp" in path:
                                print(path + "文件发现疑是：jspwebshell")
                                i = i + 1
                                break
                            else:
                                print(path + "文件发现疑是：" + key2)
                                i = i + 1
                                break
                    if i != 0:
                        break
                if i != 0:
                    break









