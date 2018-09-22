import random

if __name__ == "__main__":
    print(random.random())

    print(random.uniform(10, 20))

    print(random.randint(10, 20))

    print(random.randrange(0, 100, 3))

    print(random.choice("hello world!"))

    list1 = []
    [list1.append(i) for i in range(1, 11)]
    random.shuffle(list1)
    print(list1)

    print(random.sample(list1, 6))
