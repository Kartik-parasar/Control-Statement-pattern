n = int(input("Enter the number: "))

for i in range(n, 0, -1): 
    for j in range(i):     
        if j == 0 or j == i - 1:
            print("*", end="")
        else:
            print("_", end="")
    print()
