n, t = map(int,input().split())
arr = list(map(int,input().split()))
ans,cnt=0,0

for i in range(n):
    if arr[i] > t:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)