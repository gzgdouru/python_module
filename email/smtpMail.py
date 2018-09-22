# -*- coding: UTF-8 -*-
import smtplib, sys, email.utils

mailServer = "smtp.163.com"
From = "gzgdouru@163.com"
To = "1111@163.com"
Date = email.utils.formatdate()
subject = '放假通知'

text = ("From:" + From + "\n")
text += ("To:" + To + "\n")
text += ("Date:" + Date + "\n")
text += ("Subject:" + subject + "\n\n")

content = '''
欧儒，您好：  
您的 iCloud 储存空间将满。您总计 5 GB 的储存空间剩 14.3 MB。  
以每月 ¥6.00 的价格升级至 50 GB  
iCloud 储存空间用于“iCloud 照片图库”，即使在您的设备丢失时，也可以确保您 iPhone、iPad 和 iPod touch 上最重要的数据安全可用。iCloud Drive 以及 Keynote、Pages 和 Numbers 等 App 也使用 iCloud 储存空间，让您的文件随时随地保持最新。  
若要继续使用 iCloud 并备份您的照片、文稿、通讯录等，您需要升级 iCloud 储存空间方案或减少正在使用的储存空间量。  
此致，  
iCloud 团队  
重要信息：如果您的使用量超出储存空间方案，新照片和视频将不会上传至“iCloud 照片图库”，并且您的设备也将停止备份至 iCloud。iCloud Drive 和启用 iCloud 的 App 将不再跨设备更新。  
'''
text += content
print(text)
'''
print "connection..."
server = smtplib.SMTP(mailServer)
server.login(From, "5201314ouru...")
result = server.sendmail(From, To, text)
server.quit()

if result:
    print "failed recipients:", result
else:
    print "No error"
print "Bye."
'''