import re

if __name__ == "__main__":
    pattern = re.compile(r"(\w+) (\w+)")
    m = pattern.match("Hello world Hi Python")
    print(m.group())
    print(m.group(1))
    print(m.group(2))