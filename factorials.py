def factorials(n: int):
    fact = 1
    return {i: (fact := fact * i) for i in range(1, n + 1)}


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
