n=int(input())

for i in range(n):
    ans=0
    arr=input().split()
    a=int(arr[0])
    b=int(arr[1])
    for j in range(a,b+1):
        if j%2==0:
            ans+=j
    print(ans)