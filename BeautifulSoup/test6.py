#coding:utf8
#搜索文档树

from bs4 import BeautifulSoup
import bs4
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were</p>
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<p>and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html)

#find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
#传字符串
# print soup.find_all("b")
# print soup.find_all("a")

#传正则表达式
# for tag in soup.find_all(re.compile(r"^b")):
#     print tag.name

#传列表
# for tag in soup.find_all(["a", "b"]):
#     print tag

#传 True,True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
# for tag in soup.find_all(True):
#     print tag.name

#传方法
# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")
#
# for tag in soup.find_all(has_class_but_not_id):
#     print tag

# print soup.find_all(id="link1")
# print soup.find_all(href=re.compile(r"elsie"))
# print soup.find_all(href=re.compile(r"elsie"), id="link1")
# print soup.find_all("a", class_="sister")
# print soup.find_all(attrs={"class":"story"})

# print soup.find_all(text="Elsie")
# print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# print soup.find_all(text=re.compile("Elsie"))

print soup.find_all("a", limit=2)
