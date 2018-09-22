import zmail

mail = {
    'subject': 'Success!',  # Anything you want.
    'content': 'This message from zmail!',  # Anything you want.
    'attachments': r'C:\Users\ouru\Desktop\coding-78\前端html源码.zip',  # Absolute path will be better.
}

server = zmail.server('18719091650@163.com', 'qq5201314ouru')

server.send_mail('anjubaoouru@163.com', mail)