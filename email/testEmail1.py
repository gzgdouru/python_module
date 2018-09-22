import smtplib
from email.mime.text import MIMEText
from email.header import Header
import email.utils

senders = ["anjubaoouru@163.com", "gzouru@163.com"]
receiver = ["gzgdouru@163.com"]
subject = "放假通知"
smtpServer = "smtp.163.com"
passWd = "qq5201314ouru"
chart = "utf-8"
content = "大家关好窗户"
Date = email.utils.formatdate()

for sender in senders:
    msg = MIMEText(content, "plain", chart)
    msg["Subject"] = Header(subject, chart)
    msg["Date"] = Date
    msg["From"] = sender
    msg["To"] = ",".join(receiver)

    server = smtplib.SMTP(smtpServer)
    server.login(sender, passWd)
    result = server.sendmail(sender, receiver, msg.as_string())

    if result:
        print("failed:", result)
    else:
        print("no error!")

    # server.quit()
