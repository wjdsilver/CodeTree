n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
c = [int(input()) for _ in range(m)]

for i in range(m):
    for j in range(n):#해당 줄의 가장 위에 있는 칸을 터트림
        if grid[j][c[i]-1]!=0:
            x=j
            y=c[i]-1#터트릴 칸
            break
        else:
            continue

    r_start = max(0, x-grid[x][y]+1)
    r_end = min(n-1, x+grid[x][y]-1)
    c_start = max(0, y-grid[x][y]+1)
    c_end = min(n-1, y+grid[x][y]-1)

    for j in range(c_start,c_end+1):
        grid[x][j]=0

    for j in range(r_start,r_end+1):
        grid[j][y]=0

    for b in range(n):
        nonzero = [grid[a][b] for a in range(n) if grid[a][b] != 0]
        for a in range(n - len(nonzero)):
            grid[a][b] = 0
        for a in range(len(nonzero)):
            grid[n - len(nonzero) + a][b] = nonzero[a]


for elem in grid:
    print(*elem)