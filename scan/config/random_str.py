#coding:utf-8
import time
import random

def random_str():
    data = "123456789zxcvbnmasdfghjklqwertyuiop"
    random.seed(time.time())
    sa = []
    for i in range(6):
        sa.append(random.choice(data))
        random_s = "jinny_" + "".join(sa)
    return random_s