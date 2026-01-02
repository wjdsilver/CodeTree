n, m, r, c = map(int, input().split())
grid=[[0]*n for _ in range (n)] #n*n공간
grid[r-1][c-1]=1
cnt=0

def action(x,y):
    if inRange(x,y):
        bomb(x,y)

def inRange(x,y):
    return 0<=x<n and 0<=y<n

def bomb(x,y):
    ngrid[x][y]=1

for i in range(m):
    d=2**(i)
    ngrid = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if grid[j][k]==1:
                ngrid[j][k]=1
                action(j-d,k)
                action(j+d,k)
                action(j,k-d)
                action(j,k+d)
    grid=ngrid

for a in range(n):
    for b in range(n):
        if grid[a][b]==1:
            cnt+=1
print(cnt)
