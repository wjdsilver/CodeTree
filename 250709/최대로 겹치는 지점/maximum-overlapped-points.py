n = int(input())
arr=[0]*101
ans=0

for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        arr[j]+=1

for i in range(101):
    if arr[i]>ans:
        ans=arr[i]
print(ans)


