# Please write a function named histogram, which takes a string as its argument. The function should print out a
# histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be
# represented by a star on the specific line for that letter.

def histogram(s: str):
    dic = {}
    for ch in s:
        if ch not in dic:
            dic[ch] = 0
        dic[ch] += 1
    for key, value in dic.items():
        print(key, "*" * value)


if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")
