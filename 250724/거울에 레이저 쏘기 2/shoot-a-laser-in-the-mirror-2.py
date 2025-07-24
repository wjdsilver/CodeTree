import sys

n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
#dxs, dys = [0,-1,0,1], [1,0,-1,0 ]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def findStartPoint(k):
    k-=1
    if k//n==0:
        x,y=k%n,0
        d=1
    elif k//n==1:
        x,y=n-1,k%n
        d=2
    elif k//n==2:
        x,y=(3*n-1-k)%n,n-1
        d=3
    elif k//n==3:
        x,y=0,(4*n-1-k)%n
        d=0
    return x,y,d

def findWay(s,d):
    if s=="/":
        return [3, 2, 1, 0][d]
    elif s == "\\":
        return [1, 0, 3, 2][d]

x, y, d = findStartPoint(k)
cnt = 1

while True:
    #print(x,y,d)
    d=findWay(grid[y][x],d)
    nx,ny=x+dxs[d],y+dys[d]
    #print(nx,ny,d)
    if not inRange(nx,ny):
        print(cnt)
        sys.exit()
    x,y=nx,ny
    #print(x,y)
    cnt+=1
