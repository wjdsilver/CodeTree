n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#8방향
dxs=[-1,-1,-1,0,0,1,1,1]
dys=[-1,0,1,-1,1,-1,0,1]

def inRange(x,y):
    return 0<=x<n and 0<=y<n


def switch(x,y):
    best_x=x
    best_y=y
    best_value = 0

    for i in range(8):
        nx = x + dxs[i]
        ny = y + dys[i]
        if inRange(nx, ny) and grid[nx][ny] > best_value:
            best_value = grid[nx][ny]
            best_x, best_y = nx, ny

    grid[x][y], grid[best_x][best_y] = grid[best_x][best_y], grid[x][y]

def turn():
    for x in range(1,n**2+1):#1부터 차례대로
        found=False
        for i in range(n):
            for j in range(n):
                #1부터 차례대로 교체 진행
                if grid[i][j]==x:
                    switch(i,j)
                    found=True
                    break
            if found:
                break
            
    return grid
                   


for i in range(m):
    turn()

for row in grid:
    print(*row)
