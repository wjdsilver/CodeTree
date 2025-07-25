n = int(input())
grid = [[0] * n for _ in range(n)]

r,c=n//2,n//2
cnt, d=1, 0
grid[r][c]=cnt

def inRange(r,c):
    return 0<=r<n and 0<=c<n

dxs,dys=[1,0,-1,0],[0,1,0,-1]

while 1 <= cnt <= n*n:
    d=(d+1)%4
    nr,nc=r+step*dxs[d],c+step*dys[d]
    print(nr,nc,d,cnt)
    if not inRange(nr,nc) or grid[nr][nc]!=0:
        d=(d+1)%4
        nr,nc=r+dxs[d],c+dys[d]
    r,c=nr,nc
    
    grid[r][c]=cnt
    if cnt%2==1:
        d=(d+4-1)%4
for row in grid:
    print(*row)
