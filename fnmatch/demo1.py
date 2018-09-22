from fnmatch import fnmatch, fnmatchcase

if __name__ == "__main__":
    print(fnmatch("foo.txt", "*.txt"))

    print(fnmatch('foo.txt', '?oo.txt'))

    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

    print(fnmatch('foo.txt', '*.TXT'))

    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in names if fnmatch(name, 'Dat*.csv')])
