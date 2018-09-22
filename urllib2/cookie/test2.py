#coding:utf8
#保存Cookie到文件
import urllib2
import cookielib

fileName = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename=fileName)
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)
response = opener.open("http://www.baidu.com")

#ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
cookie.save(ignore_discard=True, ignore_expires=True)

