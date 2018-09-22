import re

if __name__ == "__main__":
    pattern = re.compile(r"\d")
    result = pattern.match("123")
    print(result.group())

    pattern = re.compile(r"abc d", re.I|re.X)
    result = pattern.match("AbcD")
    print(result.group())