import re

if __name__ == "__main__":
    text = "I'm crash a lamp-post"
    pattern = re.compile(r"[a-zA-Z]+\b")
    print(pattern.findall(text))