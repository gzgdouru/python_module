from operator import itemgetter
from collections import namedtuple

if __name__ == "__main__":
    Person = namedtuple("person", "name age")
    persons = []
    persons.append(Person(name="ouru", age=25))
    persons.append(Person(name="wanzhao", age=31))
    persons.append(Person(name="panqing", age=32))

    print(sorted(persons))
    print(sorted(persons, key=lambda x:x[1]))
    print(sorted(persons, key=itemgetter(1)))

    print([itemgetter(1, 0)(person) for person in persons])
