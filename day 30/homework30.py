my_num = int(input("Please enter a number: "))


for i in range(1, my_num + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")