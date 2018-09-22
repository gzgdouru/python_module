import yaml

if __name__ == "__main__":
    x = yaml.load(open("config.yaml", "r", encoding="utf-8"))
    print(x)

    print(x.get("languages"))