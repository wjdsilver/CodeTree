n = int(input())
arr = [int(input()) for _ in range(n)]
ans,cnt=0,0

for i in range(1,n):
    if arr[i-1]*arr[i]>0:
        cnt+=1
    elif arr[i-1]*arr[i]<0:
        if ans<cnt:
            ans=cnt
        cnt=1
if ans<cnt:
    print(cnt)
else:
    print(ans)