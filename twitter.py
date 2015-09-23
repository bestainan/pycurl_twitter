#-*- coding:UTF-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar
import re
import acc
import random
import myfile
from time import sleep

mail = ['@hotmail.com','@gmail.com','@163.com','@year.com','@outlook.com','@yahoo.com']



class Twitter():
	
    def creat():
        url = 'https://twitter.com/'
        account = acc.creat_1_account()
        password = acc.creat_1_pasword()
        email = account+random.choice(mail)
        data = {}
        
        
        cookie = http.cookiejar.CookieJar()#保存cookie
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')]
        urllib.request.install_opener(opener)


        resp = urllib.request.urlopen(url).read().decode('utf-8')

        creat_twitter = 'https://twitter.com/account/create'
        find = 'input type="hidden" name="authenticity_token" value="(?P<tokenVal>\w+)">'
        
        haha = re.search(find,resp)
        token = haha.group('tokenVal')

        data['authenticity_token'] = token
        data['user[name]'] = account
        data['user[email]'] = email
        data['user[user_password]'] = password
        data['user[screen_name]'] = account
        data['asked_cookie_personalization_setting'] = '1'
        data['context'] = 'signup'
        data['ad_id'] =''
        data['ad_ref'] =''
        data['user[remember_me_on_signup]'] = '1'
        data['user[discoverable_by_email]'] = '1'
        data['user[send_email_newsletter]'] = '1'
        postData = urllib.parse.urlencode(data);
        postData = postData.encode('utf-8')
        temp =urllib.request.urlopen(creat_twitter,data=postData)
        
        
        if temp.geturl() == 'https://twitter.com/i/start':
            save = email + '\t' + password + '\n'
            f = open('acc.ini','a+')
            f.write(save)
            f.close()
            return '注册成功@。@'
        
        elif temp.geturl() == 'https://twitter.com/welcome/phone_number':
            return '注册失败， 转到激活'
        
    def Activation(self):
        from selenium import webdriver
        import os
        while True:
        
            url = 'https://member.x-legend.co.jp/openid/twitter/login.php'
            url2 = 'https://member.x-legend.co.jp/member/register_opi_1.php'
            
            email, password = FileUser.read_file_acc_paswd(self,'acc.ini')
    
            
            d = webdriver.Chrome()
            d.implicitly_wait(60)
            
            d.get(url)
            d.find_element_by_xpath('//*[@id="username_or_email"]').send_keys(email)
            d.find_element_by_xpath('//*[@id="password"]').send_keys(password)
            d.find_element_by_xpath('//*[@id="allow"]').submit()
        
                
            if 'エラー' in d.title:
                print('该换IP了！~')
                d.quit()
                break
            sex_ch = ['#main_wrapper > div > div > div > div > table > tbody > tr:nth-child(3) > td > input[type="radio"]:nth-child(2)',
                      '#main_wrapper > div > div > div > div > table > tbody > tr:nth-child(3) > td > input[type="radio"]:nth-child(1)']
            year_ch = '#year > option:nth-child(%s)' % random.randint(17,57)
            month_ch = '//*[@id="main_wrapper"]/div/div/div/div/table/tbody/tr[2]/td/select[2]/option[%s]' % random.randint(1,12)
            day_ch = '//*[@id="main_wrapper"]/div/div/div/div/table/tbody/tr[2]/td/select[3]/option[%s]' % random.randint(1,29)
            
            
            
            d.find_element_by_xpath('//*[@id="mainBn_Area"]/div[1]/ul[1]/li[2]/a/img').click()
            d.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div[2]/div[1]/div[1]/ul/li[2]/a').click()
            
            sleep(3)
            
            
            d.find_element_by_css_selector(random.choice(sex_ch)).click()
            d.find_element_by_css_selector(year_ch).click()
            
            
            d.find_element_by_xpath(month_ch).click()
            d.find_element_by_xpath(day_ch).click()
            
            d.find_element_by_css_selector('#main_wrapper > div > div > div > div > table > tbody > tr:nth-child(4) > td > div:nth-child(3) > input').click()
            d.find_element_by_css_selector('#main_wrapper > div > div > div > div > table > tbody > tr:nth-child(4) > td > div:nth-child(4) > input').click()
            
            d.find_element_by_xpath('//*[@id="submit"]/img').submit()
            
            d.find_element_by_xpath('//*[@id="agree"]').click()
            sleep(3)
            d.find_element_by_css_selector('#next > img').click()
            if 'この度はX-LEGEND GAMESにご登録' in d.find_element_by_css_selector('#main_wrapper > div > div > div > p:nth-child(3)').text:
                f = open('jihuo.ini','a')
                save = email + '\t' + password + '\n'
                f.write(save)
                f.close()
                FileUser.save_file(self,fname1='acc.ini', fname2='jihuo.ini')
                d.quit()
                print('注册OK')
                
                    


    
if __name__ == ('__main__'):
    app = Twitter()
    #app.creat() 
    app.Activation()