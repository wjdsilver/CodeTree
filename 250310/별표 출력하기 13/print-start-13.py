n=int(input())
m=1
for i in range(1,2*n+1):
    if i%2==1:
        for j in range(n):
            print("* ",end="")
        n-=1
        print()
    elif i%2==0:
        for j in range(m):
            print("* ",end="")
        m+=1
        print()