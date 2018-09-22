#coding:utf8
#遍历文档树

from bs4 import BeautifulSoup
import bs4

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#直接子节点
soup = BeautifulSoup(html)
# print soup.head.contents
# print soup.head.contents[0]
#
# print soup.body.children
# for child in soup.body.children:
#     print child

#所有子孙节点
# for child in soup.descendants:
#     print child

#节点内容
# print soup.head.string
# print soup.title.string
# print soup.html.string

#多个内容
# for item in soup.strings:
#     print item
# print "-" * 80
#
# #.stripped_strings 可以去除多余空白内容
# for item in soup.stripped_strings:
#     print item

#父节点
# p = soup.p
# print p.parent.name
# content = soup.head.title.string
# print content.parent.name

#全部父节点
# content = soup.head.title.string
# for parent in content.parents:
#     print parent.name

#兄弟节点(next_sibling, previous_sibling)
# print soup.p.next_sibling #None
# print soup.p.previous_sibling #None
# print soup.p.next_sibling.next_sibling

#全部兄弟节点(next_siblings, previous_siblings)
# for sibling in soup.a.next_siblings:
#     print sibling

#前后节点(next_element, previous_element)
# print soup.head.next_element

#所有前后节点(next_elements, previous_elements)
for element in soup.a.next_elements:
    print(repr(element))
