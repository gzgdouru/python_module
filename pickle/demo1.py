import pickle

if __name__ == "__main__":
    list1 = []
    [list1.append(i) for i in range(1, 11)]
    print(list1)

    list1Str = pickle.dumps(list1)
    print(list1Str)

    list2 = pickle.loads(list1Str)
    print(list2)

    with open("1.txt", "wb") as fileObj:
        pickle.dump(list2, fileObj)