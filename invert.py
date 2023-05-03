# Please write a function named invert(dictionary: dict), which takes a
# dictionary as its argument. The dictionary should be inverted in place
# so that values become keys and keys become values.

def invert(dictionary: dict):
    res = {}
    for key, val in dictionary.items():
        res[val] = key
    dictionary.clear()
    for key, val in res.items():
        dictionary[key] = val


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
