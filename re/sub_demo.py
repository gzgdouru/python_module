import re

if __name__ == "__main__":
    pattern = re.compile(r'\s+')
    text = "Process finished with exit code 0"
    m = pattern.sub('-', text, 3)
    print(m)

    m = pattern.subn("-", text)
    print(m)