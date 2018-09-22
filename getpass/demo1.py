import getpass

if __name__ == "__main__":
    user = getpass.getuser()
    pwd = getpass.getpass("ener password for {user}: ".format(user=user))
    print(user, pwd)