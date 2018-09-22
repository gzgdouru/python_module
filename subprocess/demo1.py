import subprocess

if __name__ == "__main__":
    # resCode = subprocess.call("ls -l")
    # print(resCode)

    # resCode = subprocess.check_call("ls -l hello.py")
    # print(resCode)

    text = subprocess.check_output("ls -l demo1.py")
    print(text.decode("gbk"))