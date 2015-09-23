#-*- coding:utf-8 -*-

import random
import string



def creat_1_account():
    letter_num = string.ascii_letters +string.digits
    c = string.ascii_letters
    
    
    mycount = ''
    for j in range(random.randint(7,12)):#数字8 是账号密码的长度
        b = letter_num[random.randint(0,61)]
        mycount += b
        if mycount[0] in string.digits:
            mycount = c[random.randint(0,51)] + mycount[1:]
    return mycount


def creat_1_pasword():
    letter_num = string.ascii_letters +string.digits + '~!@#$%^&*()_+|}{:?><-=[];.,'
    password = ''
    for j in range(13):#密码的长度
        b = random.choice(letter_num)
        password += b
    return password

