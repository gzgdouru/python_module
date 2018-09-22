#coding:utf8
import paramiko

remoteHost = ("192.168.232.134", 22)

# 实例化一个trans对象
trans = paramiko.Transport(remoteHost)

# 建立连接
trans.connect(username="ouru", password="5201314ouru")

# 实例化一个 sftp对象,指定连接的通道
sftp = paramiko.SFTPClient.from_transport(trans)

# 发送文件
sftp.put(localpath='test1.py', remotepath='/usr/local/ouru/python/test1.py')
# 下载文件
# sftp.get(remotepath, localpath)
trans.close()