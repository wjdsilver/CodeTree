n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
fin=0

for i in range(1,n+1):
    ans=0
    for j in range(1,n+1):
        ans=pairs.count((i,j)) + pairs.count((j,i))
        fin=max(fin,ans)
print(fin)