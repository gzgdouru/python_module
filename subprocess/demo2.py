import subprocess

if __name__ == "__main__":
    # child = subprocess.Popen('ping baidu.com', shell=True)
    # child.wait()
    # print("parent process")

    child = subprocess.Popen('ping baidu.com', stdout=subprocess.PIPE, shell=True)
    print(child.stdout.read().decode("gbk"))
    print("parent process")