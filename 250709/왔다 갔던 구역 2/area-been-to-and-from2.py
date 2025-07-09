n = int(input())
arr=[0]*2001
cur=1000
ans=0

for _ in range(n):
    x, di = input().split()
    x=int(x)

    if di=="L":
        for j in range(cur-x+1,cur+1):
            arr[j]+=1
        cur=cur-x
    elif di=="R":
        for j in range(cur,cur+x):
            arr[j]+=1
        cur=cur+x

for i in range(2000):
    if arr[i]>1:
        ans+=1
print(ans)
