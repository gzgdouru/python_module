import re

if __name__ == "__main__":
    # pattern = re.compile(r"abc d", re.I | re.X)
    # result = pattern.search("0A2aBcd7")
    # print(result.group())
    #
    # pattern = re.compile(r"abc d", re.I | re.X)
    # matchRes = pattern.match("0AbcD5")
    # if matchRes: print("match: %s" % matchRes.group())
    # searchRes = pattern.search("0AbcD5")
    # if searchRes: print("search: %s" % searchRes.group())

    # pattern = re.compile(r"(\w+)\.?(\w+)?")
    # m = pattern.match("Hello")
    # print(m.groups())
    # print(m.groups("python"))

    pattern = re.compile(r"(?P<first_str>\w+) (?P<last_str>\w+)")
    m = pattern.match("Hello python")
    print(m.groupdict())