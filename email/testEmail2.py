#coding:utf-8

import smtplib
from email.mime.text import MIMEText
import email.utils

sender = "18719091650@163.com"
receiver = "gzgdouru@163.com"
subject = "test python email"
smtpServer = "smtp.163.com"
passWd = "qq5201314ouru"
charset = "utf-8"
Date = email.utils.formatdate()
content = '''
<html>
    <h1>你好</h1>
    <div></div>
</html>
'''

msg = MIMEText(content, "html", charset)
msg["Subject"] = subject
msg["Date"] = Date
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP(smtpServer)
server.login(sender, passWd)
result = server.sendmail(sender, receiver, msg.as_string())

if result:
    print("failed:", result)
else:
    print("no error!")

server.quit()