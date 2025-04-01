n=int(input())
a=11
for i in range (1,n+1):
    b=a
    for j in range(1, n+1):
        print(b,end=" ")
        b+=2
    print()
    a+=2
    