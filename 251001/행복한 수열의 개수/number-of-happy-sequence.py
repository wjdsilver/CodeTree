n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=0

for i in range(n):#세로에 대해
    cnt=1
    for j in range(1,n):
        if grid[i][j-1]==grid[i][j]:
            cnt+=1
        if cnt>=m:
            ans+=1
            break
for i in range(n):#세로에 대해
    cnt=1
    for j in range(1,n):
        if grid[j-1][i]==grid[j][i]:
            cnt+=1
        if cnt>=m:
            ans+=1
            break

print(ans)