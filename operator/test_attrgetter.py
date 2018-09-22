from operator import attrgetter
from collections import namedtuple

if __name__ == "__main__":
    Person = namedtuple("Person", "name age height weight")
    people = [
        Person("ouru", 25, 163, 114),
        Person("wanzhao", 31, 172, 112),
        Person("panqing", 32, 168, 169),
    ]

    print(people)

    print(sorted(people, key=attrgetter("age"), reverse=True))