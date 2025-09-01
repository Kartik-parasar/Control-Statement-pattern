# Number-Star pattern with user input

n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        if j % 2 == 0:  
            print("*", end=" ")
        else:         
            print(num, end=" ")
            num += 2
    print()
