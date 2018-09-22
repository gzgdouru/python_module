import re

if __name__ == "__main__":
    pattern = re.compile(r"\d+")
    m = pattern.finditer('a1b2c33d4')
    print(m)

    for num in m:
        print(num.group())