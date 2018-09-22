from functools import partial
from operator import mul

if __name__ == "__main__":
    triple = partial(mul, 3)
    print(triple(7))

    print([triple(i) for i in range(10)])