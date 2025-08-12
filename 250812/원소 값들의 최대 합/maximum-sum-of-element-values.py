n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
fin=0

for i in range(1,n+1):#시작위치
    pos=i
    ans=0
    for _ in range(m):
        ans += arr[pos]
        pos = arr[pos]
    fin=max(ans,fin)
print(fin)
        
