n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
#newgrid=[[0]*n for _ in range (n)]
r, c = map(int, input().split())
r-=1
c-=1
x=grid[r][c]-1 #특정 위치 값-1

r_start = max(0, r - x)
r_end = min(n - 1, r + x)
c_start = max(0, c - x)
c_end = min(n - 1, c + x)

for i in range(c_start,c_end+1):
    grid[r][i]=0

for i in range(r_start,r_end+1):
    grid[i][c]=0

for j in range(n):
    nonzero = [grid[i][j] for i in range(n) if grid[i][j] != 0]
    for i in range(n - len(nonzero)):
        grid[i][j] = 0
    for i in range(len(nonzero)):
        grid[n - len(nonzero) + i][j] = nonzero[i]

for elem in grid:
    print(*elem)
