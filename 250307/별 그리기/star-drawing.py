n=int(input())

for i in range(1,n+1):
    for _ in range(n-i):
        print(" ",end="")
    for _ in range(2*i-1):
        print("*",end="")
    print()
for i in range(n+1,2*n):
    for _ in range(i-n):
        print(" ",end="")
    for _ in range(2*(2*n-i)-1):
        print("*",end="")
    print()


