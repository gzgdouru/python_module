import re

if __name__ == "__main__":
    pattern = re.compile(r"\d+")
    m = pattern.findall('a1b2c33d4')
    print(m)

    m = pattern.findall('a1b2c33d4', 1, 6)
    print(m)