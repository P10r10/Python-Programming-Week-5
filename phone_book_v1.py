dic = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        break
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        dic[name] = number
        print("ok!")
    if command == 1:
        name = input("name: ")
        if name in dic:
            print(dic[name])
        else:
            print("no number")
print("quitting...")
