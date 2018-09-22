import itertools

if __name__ == "__main__":
    #chain
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    booleans = [1, 0, 1, 0, 0, 1, 1]
    # print(list(itertools.chain(letters, booleans)))
    # print(tuple(itertools.chain(letters, letters[3:])))

    #count
    # for item in itertools.count(100, 2):
    #     if item != 100 and item % 100 == 0: break
    #     print(item, end=" ")

    #filterfalse
    numbers = [23, 20, 44, 32, 7, 12]
    # print(list(itertools.filterfalse(None, booleans)))
    # print(list(itertools.filterfalse(lambda x:x < 20, numbers)))

    #compress
    # print(list(itertools.compress(letters, booleans)))

    #starmap
    # print(list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))
    # for i in itertools.starmap(max,[[5,14,5],[2,34,6],[3,5,2]]):
    #     print(i, end=" ")

    #repeat
    # print(list(itertools.repeat(10, 3)))

    #dropwhile
    # print(list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

    #takewhile
    # print((list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]))))

    #islice
    # for i in itertools.islice("abcdef", 0, 4, 2):
    #     print(i, end=" ")

    #product
    # print(list(itertools.product("ABCD", "XY")))
    # print(list(itertools.product(range(2), repeat=3)))
    # for i in itertools.product([1, 2, 3], [4, 5], [6, 7]):
    #     print(i, end=" ")

    #permutations
    # for i in itertools.permutations([1, 2, 3], 2):
    #     print(i, end=" ")

    #combinations
    # for i in itertools.combinations([1, 2, 3], 2):
    #     print(i, end=" ")

    #combinations_with_replacement
    # for i in itertools.combinations_with_replacement([1, 2, 3], 2):
    #     print(i, end=" ")

    #求质数序列中1,3,5,7,9,11,13,15三个数之和为35的三个数
    print([data for data in itertools.combinations([1,3,5,7,9,11,13,15], 3) if sum(data) == 35])