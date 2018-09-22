from operator import methodcaller

if __name__ == "__main__":
    s = "The time has come"
    print(methodcaller("upper")(s))

    print(methodcaller("replace", " ", "-")(s))