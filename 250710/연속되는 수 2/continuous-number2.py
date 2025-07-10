n = int(input())
arr = [int(input()) for _ in range(n)]
cnt=0
ans=0

for i in range(n):
    if arr[i]==0 or arr[i-1]==arr[i]:
        cnt+=1
        if cnt>ans:
            ans=cnt
    else:
        cnt=1
print(ans)