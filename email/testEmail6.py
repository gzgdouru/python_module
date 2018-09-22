# -*- coding: UTF-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = '18719091650@163.com'
receivers = 'gzgdouru@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
passWd = "5201314ouru..."

msgRoot = MIMEMultipart('related')
msgRoot['From'] = sender
msgRoot['To'] = receivers
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject,"utf-8")

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<html>
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
</html>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))


# 指定图片为当前目录
fp = open(r"F:\111.png", 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtpObj = smtplib.SMTP('smtp.163.com')
smtpObj.login(sender, passWd)
smtpObj.sendmail(sender, receivers, msgRoot.as_string())
print("邮件发送成功")

