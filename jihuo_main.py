#-*- coding:utf-8 -*-
from url_fun import MY_PYCURL
from urllib import parse
import urllib
import re
import random
from myfile import read_file_acc_paswd, save_file
import os
import urllib.request
import http.cookiejar
import acc
import twitter
import sys

def jihuo_jp():
    jp_account_in_url = 'https://member.x-legend.co.jp/openid/twitter/login.php'
    jp_data_url = 'https://member.x-legend.co.jp/member/register_opi_2.php'
    jp_account_in_url2 = 'https://twitter.com/intent/sessions'
    jp_account_in_url3 = 'https://member.x-legend.co.jp/member/register_opi_3.php'
    app = MY_PYCURL()
    c = app.InitCurl()
    
    new_url, new_value = app.GetUrl(c,jp_account_in_url,'utf-8')
    authenticity_token = app.Find_authenticity_token(new_value)
    oauth_token = app.Find_oauth_token(new_value)

    account, password = read_file_acc_paswd('acc.ini')
    
    data={}
    data['authenticity_token'] = authenticity_token
    data['repost_after_login'] = 'https://api.twitter.com/oauth/authorize'
    data['oauth_token'] = oauth_token
    data['session[username_or_email]'] = account
    data['session[password]'] = password
    
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')    
    
    new_url1,new_value1 = app.Post_Data(c, jp_account_in_url2, data, 'utf-8')

    new_url_302 = app.Find_url(new_value1)

    new_url, new_value = app.GetUrl(c, new_url_302, 'utf-8')
    if new_url == 'https://member.x-legend.co.jp/error/reg_limit.php':
        os.remove('cookie_file_name')
        return '都不行了，只能换iP了！~'
        
    new_url, new_value = app.GetUrl(c, jp_data_url, 'utf-8')
    year = random.randint(1970,2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    sex = 'F','M'
    sex = random.choice(sex)
    data = {}
    data['year'] = year
    data['month'] = month
    data['day'] = day
    data['sex'] = sex
    data['selected_games[]'] = '2'
    data['selected_games[]'] = '1'
    
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    
    new_url,new_value = app.Post_Data(c, jp_data_url, data, 'utf-8')
    
    new_url, new_value = app.GetUrl(c, jp_account_in_url3, 'utf-8')
    with open('jihuo.ini','a+') as f:
        temp = account + '\t' + password + '\n'
        f.write(temp)
    #os.remove('cookie_file_name')
    save_file('acc.ini', 'jihuo.ini')    
    return '激活成功'

if __name__ == '__main__':
    while 1:
        temp = twitter.Twitter.creat()  #注册
        print(temp)
        if temp == '注册失败， 转到激活':
            while 1:
                temp = jihuo_jp()  #激活
                print(temp)
                if temp == '都不行了，只能换iP了！~':
                    sys.exit() 


    
        
    
    
    
    
