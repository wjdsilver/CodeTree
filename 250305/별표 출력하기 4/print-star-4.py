n=int(input())
for i in range (1,2*n):
    if i<=n:
        for j in range(n+1-i):
            print("*",end=" ")
    elif i>n:
        for k in range (1,i-n+2):
            print("*",end=" ")
    print()