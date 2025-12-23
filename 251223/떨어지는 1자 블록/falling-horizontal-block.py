n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

r=0

for i in range(n):
    blank=True
    for j in range(k-1,k+m-1):
        if grid[i][j]==1:
            blank=False
            break
    if blank==False:
        r=i-1
        break


for x in range (m):
    grid[r][k-1+x]=1

for elem in grid:
    print(*elem)
