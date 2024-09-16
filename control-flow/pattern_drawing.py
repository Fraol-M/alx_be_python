postive_num = int(input("Enter the size of the pattern: "))

row = 0
while row < postive_num:
    for i in range(postive_num):
        print("*", end = "")
    print()
    row+=1