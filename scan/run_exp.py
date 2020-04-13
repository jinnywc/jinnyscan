import sys
import os
sys.path.insert(0,'.')
from exp import *



dirname = "./exp"
names = list()
def run_exp(url):
    for maindir, subdir, filenamelist in os.walk(dirname):
        for filename in filenamelist:
            if "exp_" not in filename or ".pyc" in filename:
                continue
            name = filename.split(".",1)[0]
            names.append(name)

    for name in names:
        exec("from exp import " + name)
        name1 = eval(name + "." + name)
        name1(url)


# run_exp("http://127.0.0.1:9998/")
# exp_cve_2018_1335("http://127.0.0.1:9998/")
