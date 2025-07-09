n, k = map(int, input().split())
arr=[0]*n
ans=0

for i in range(k):
    a,b=map(int,input().split())
    for j in range(a-1,b):
        arr[j]+=1

for i in range(n):
    if arr[i]>ans:
        ans=arr[i]
print(ans)
