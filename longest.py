# Please write a function named longest(strings: list), which takes a list
# of strings as its argument. The function finds and returns the longest
# string in the list. You may assume there is always a single longest string
# in the list.

def longest(strings: list):
    max_len = 0
    max_str = ""
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            max_str = string
    return max_str


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
