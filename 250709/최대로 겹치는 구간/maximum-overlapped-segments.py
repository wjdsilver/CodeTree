n = int(input())
arr=[0]*200
ans=0

for i in range(n):
    a,b=map(int,input().split())
    for j in range(a+100,b+100):
        arr[j]+=1

for i in range(200):
    if arr[i]>ans:
        ans=arr[i]
print(ans)
