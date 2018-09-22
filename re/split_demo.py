import re

if __name__ == "__main__":
    pattern = re.compile(r"\d+")
    m = pattern.split('a1b2c3d4e')
    print(m)

    m = pattern.split('a1b2c3d4e', 3)
    print(m)