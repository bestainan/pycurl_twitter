#-*- coding:utf-8 -*-
import pycurl
from io import BytesIO
import urllib  
import re
class MY_PYCURL():
    
    def InitCurl(self):
        c = pycurl.Curl()  
        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中  
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name") #动态获取cookie 
        c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源  
        c.setopt(pycurl.MAXREDIRS, 5)  
        #设置代理 如果有需要请去掉注释，并设置合适的参数  
        #c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)  
        #c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)  
        return c
    
    def GetUrl(self,c, url, charset):

        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中  
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name") #动态获取cookie 
        c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源  
        c.setopt(pycurl.MAXREDIRS, 5)  
        
        
        b=BytesIO()
        #回调
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        #链接超时
        c.setopt(pycurl.CONNECTTIMEOUT, 120) 
        #定义USERAGENT
        c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36") #模拟浏览器
        #自动获取REFERER
        #c.setopt(pycurl.AUTOREFERER,1)
        #处理COOKIE
        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
        
        
        #打开网址
        c.setopt(pycurl.URL,url)
        c.perform()
            
        new_url = c.getinfo(pycurl.EFFECTIVE_URL)
        new_value = b.getvalue().decode(charset)
        b.close()
        return new_url, new_value
        
    def Post_Data(self,c,url,data,charset):
        b=BytesIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)  
        c.setopt(pycurl.POSTFIELDS,  data)  
        c.setopt(pycurl.URL, url)  
        c.perform() 
        new_url = c.getinfo(pycurl.EFFECTIVE_URL)
        new_value = b.getvalue().decode(charset)
        b.close()
        return new_url,new_value
    
    def Find_authenticity_token(self, web_value):
        import re
        find = r'<input name="authenticity_token" type="hidden" value="(?P<authenticity_token>\w+)" /></div>'
        
        r1 = re.search(find,web_value)
        authenticity_token = r1.group('authenticity_token') 
        return authenticity_token
    
    def Find_oauth_token(self, web_value):
        
        find = r'<input id="oauth_token" name="oauth_token" type="hidden" value="(?P<oauth_token>\w+)" /> ' 
        
        r1 = re.search(find,web_value)
        oauth_token = r1.group('oauth_token') 
        return oauth_token
    
    def Find_url(self, web_value):      
        find = r'<meta\s+.*url=(.+?)">'
        new_url_302 = re.findall(find,web_value)

        return new_url_302[0]