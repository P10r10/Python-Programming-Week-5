dic = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        break
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in dic:
            dic[name] = []
        dic[name].append(number)
        print("ok!")
    if command == 1:
        name = input("name: ")
        if name in dic:
            for num in dic[name]:
                print(num)
        else:
            print("no number")
print("quitting...")
