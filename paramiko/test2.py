#coding:utf8
import paramiko

# 实例化一个transport对象
trans = paramiko.Transport(("192.168.232.134", 22))

# 建立连接
trans.connect(username="ouru", password="5201314ouru")

# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans

# 执行命令，和传统方法一样
# 执行命令
stdin, stdout, stderr = ssh.exec_command("pwd")

# 结果放到stdout中，如果有错误将放到stderr中
print stdout.read()

# 关闭连接
ssh.close()