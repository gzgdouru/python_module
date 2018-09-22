import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")

    print(config.sections())

    print(config.items('topsecret.com'))

    print(config.options('topsecret.com'))

    print(config['bitbucket.org']['User'])
    print(config.get("bitbucket.org", "User"))