import sys
N, H, T = map(int, input().split())
arr = list(map(int, input().split()))
small=sys.maxsize

for i in range(N-T+1):
    ans=0
    for j in range(T):
        ans+=abs(arr[i+j]-H)
    small=min(ans,small)
print(small)