from operator import mul
from functools import reduce

if __name__ == "__main__":
    value = reduce(lambda x, y: x*y, range(1, 11))  # 1到10的阶乘
    print(value)

    value = reduce(mul, range(1, 11))   # 1到10的阶乘
    print(value)