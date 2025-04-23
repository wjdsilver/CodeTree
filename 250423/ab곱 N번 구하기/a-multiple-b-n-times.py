n=int(input())
for i in range(n):
    arr=input().split()
    a=int(arr[0])
    b=int(arr[1])
    multi=1
    for i in range(a,b+1):
        multi*=i
    print(multi)
