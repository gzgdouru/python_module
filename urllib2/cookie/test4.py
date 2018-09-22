#coding:utf8
#利用cookie模拟网站登录
import urllib2
import requests
import cookielib

url = "http://127.0.0.1:8000/admin"
data = {
    "username" : "ouru",
    "password" : "5201314ouru"
}

response = requests.post(url, data=data)
print response.text