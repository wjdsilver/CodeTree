n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for _ in range (i):
            print("* ",end="")
        print()
    else:
        print("* ",end="")
        print()
    