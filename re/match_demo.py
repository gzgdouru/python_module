import re

if __name__ == "__main__":
    result = re.match(r"a+\d", "aA123", re.I)
    print(result.group())

    pattern = re.compile(r"abc d", re.I | re.X)
    result = pattern.match("0AbcD5", 1, 5)
    print(result.group())