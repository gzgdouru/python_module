#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import email.utils

sender = "18719091650@163.com"
receiver = "gzgdouru@163.com"
subject = "test python email"
smtpServer = "smtp.163.com"
passWd = "5201314ouru..."
charset = "utf-8"
Date = email.utils.formatdate()
content = '''
<html>
<b>Some <i>HTML</i> text</b> and an image.<p><img src="cid:image1"></p>good!
</html>
'''

msgRoot = MIMEMultipart("related")
msgRoot["Subject"] = "test message"

msgText = MIMEText(content, "html", charset)
msgRoot.attach(msgText)

fp = open(r"F:\111.png", "rb")
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header("Content-ID", "<image1>")
msgRoot.attach(msgImage)

msgRoot["Subject"] = subject
msgRoot["Date"] = Date
msgRoot["From"] = sender
msgRoot["To"] = receiver

server = smtplib.SMTP(smtpServer)
server.login(sender, passWd)
result = server.sendmail(sender, receiver, msgRoot.as_string())
if result:
    print("failed:", result)
else:
    print("no error!")

server.quit()