# Please write a function named dict_of_numbers(), which returns a new
# dictionary. The dictionary should have the numbers from 0 to 99 as its
# keys. The value attached to each key should be the number spelled out
# in words.

def units(n: int):
    if n < 0 or n > 9:
        return "error in units"
    dic = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return dic[n]


def tens(n: int):
    if n < 2 or n > 9:
        return "error in tens"
    dic = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
           6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    return dic[n]


def teens(n: int):
    if n < 10 or n > 19:
        return "error in teens"
    dic = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
           14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
           18: "eighteen", 19: "nineteen"}
    return dic[n]


def dict_of_numbers():
    res = {}
    for i in range(10):
        res[i] = units(i)
    for i in range(10, 20):
        res[i] = teens(i)
    for i in range(20, 100):
        res[i] = tens(i // 10) + "-" + units(i % 10)
        if i % 10 == 0:
            res[i] = tens(i // 10)
    return res


if __name__ == "__main__":
    for key, val in dict_of_numbers().items():
        print(key, "-", val)
