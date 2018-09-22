#coding:utf-8
import smtplib
import email.utils
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender = "18719091650@163.com"
receiver = "gzgdouru@163.com"
subject = "test python email"
smtpServer = "smtp.163.com"
passWd = "5201314ouru..."
charset = "utf-8"
Date = email.utils.formatdate()

msg = MIMEMultipart('alternative')
#msg = MIMEMultipart("relate")
msg['Subject'] = "Link"
msg["Date"] = Date
msg["From"] = sender
msg["To"] = receiver

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

att = MIMEText(open(r"F:\111.png", 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msg.attach(att)

server = smtplib.SMTP(smtpServer)
server.login(sender, passWd)
result = server.sendmail(sender, receiver, msg.as_string())
if result:
    print("failed:", result)
else:
    print("no error!")

server.quit()
