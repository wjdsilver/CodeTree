n=int(input())
for i in range (1,2*n):
    if i<=n:
        for j in range(i):
            print("*",end=" ")
    elif i>n:
        for k in range (2*n-i):
            print("*",end=" ")
    print()