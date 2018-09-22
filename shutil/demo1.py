import shutil

if __name__ == "__main__":
    # shutil.copyfileobj(open("../zip/compressFile.py", "r"), open("1.txt", "w"))

    # shutil.copyfile("../zip/compressFile.py", "1.txt")

    # shutil.copymode("demo1.py", "1.txt")

    # shutil.copystat("demo1.py", "1.txt")

    # shutil.copytree("../../myProject/database", "database", ignore=shutil.ignore_patterns("*.pyc", "*.spec"))

    # shutil.rmtree("database")

    # shutil.move("1.txt", "1.py")

    shutil.make_archive("temp", "gztar", root_dir="../../myProject/database")
