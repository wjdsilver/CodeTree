n=int(input())

for i in range(1,2*n):
    if i<n:
        for j in range(n-i):
            print("  ",end="")
        for _ in range(i):
            print("@ ",end="")
    elif i>n:
        for j in range(2*n-i):
            print("@ ",end="")
        for _ in range(i-n):
            print("  ",end="")
    else:
        for j in range(i):
            print("@ ",end="")
    
    print()