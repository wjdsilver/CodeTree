n=int(input())

for i in range(n-1):
    for _ in range(i):
        print("  ",end="")
    for _ in range(2*(n-i)-1):
        print("* ",end="")
    print()
for j in range(n+1,2*n+1):
    for _ in range(2*n-j):
        print("  ",end="")
    for _ in range(2*(j-n)-1):
        print("* ",end="")
    print()