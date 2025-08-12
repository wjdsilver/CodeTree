n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
fin=0

for i in range(n):#시작위치
    ans=0
    for _ in range(m):
        ans += arr[n]
        n = arr[n]
    fin=max(ans,fin)
print(fin)
        
