#coding:utf-8
import smtplib
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender = "18719091650@163.com"
receiver = "gzgdouru@163.com"
subject = "test python email"
smtpServer = "smtp.163.com"
passWd = "5201314ouru..."
charset = "utf-8"
Date = email.utils.formatdate()

msgRoot = MIMEMultipart("relate")
msgRoot["Subject"] = subject
msgRoot["Date"] = Date
msgRoot["From"] = sender
msgRoot["To"] = receiver

att = MIMEText(open(r"F:\111.png", "rb").read(), "base64", charset)
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment;filename=111.png"
msgRoot.attach(att)

text = MIMEText("this is a test", "plain", charset)
msgRoot.attach(text)

server = smtplib.SMTP(smtpServer)
server.login(sender, passWd)
result = server.sendmail(sender, receiver, msgRoot.as_string())
if result:
    print("failed:", result)
else:
    print("no error!")

server.quit()

