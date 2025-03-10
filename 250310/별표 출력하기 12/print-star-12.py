n=int(input())

for _ in range(n):
    print("* ", end="")
print()

for i in range(1, n):
    for j in range(n):
        if i<=j:
            if j % 2 == 1: 
                print("* ", end="")
            else:
                print("  ",end="")
        else: 
            print("  ", end="")
    print() 
