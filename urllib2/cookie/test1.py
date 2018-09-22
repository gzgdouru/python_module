#coding:utf8
#获取Cookie保存到变量
import urllib2
import cookielib

cookie = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)
try:
    response = opener.open("baidu.com")
except Exception as e:
    print e
else:
    for item in cookie:
        print "name =", item.name
        print "value =", item.value
