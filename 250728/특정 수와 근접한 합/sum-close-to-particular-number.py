import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))
part=0
ans=sys.maxsize

total=sum(arr)

for i in range(N-1):
    for j in range(i+1,N):
        part=total-arr[i]-arr[j]
        ans=min(ans,abs(S-part))
print(ans)

