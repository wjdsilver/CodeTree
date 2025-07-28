n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans=0

for i in range(n-k+1):
    hap=0
    for j in range(k):
        hap+=arr[i+j]
    ans=max(ans,hap)
print(ans)