def my_replace(s: str, start: int, end: int, substring: str) -> str:
    return s[:start] + substring + s[end:]

n = int(input("Layers: "))
lst = []
str = chr(n + 64) * (2 * n - 1) # builds initial string based on char
print(str) # 1st row
lst.append(str) # push to the stack
for i in range(1, n): # prints all the lines until middle and pushes to the stack
    str = my_replace(str, i, len(str) - i,
                     chr(n + 64 - i) * (len(str) - 2 * i))
    print(str)
    lst.append(str)
lst.pop() # discards middle row - we don't want to repeat it
while (lst): # pops all the stored rows in the stack
    print(lst.pop())
