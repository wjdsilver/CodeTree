n, m = map(int, input().split())
cnt=1
r,c=0,0
d=0

def inRange(r,c):
    return 0<=r<n and 0<=c<m

arr=[[0]*m for _ in range (n)]
dxs,dys=[1,0,-1,0],[0,1,0,-1]

while cnt <= n*m:
    arr[r][c]=cnt
    cnt+=1
    nr,nc=r+dxs[d],c+dys[d]
    if not inRange(nr,nc) or arr[nr][nc]!=0:
        d=(d+1)%4
        nr,nc=r+dxs[d],c+dys[d]
    r,c=nr,nc
for row in arr:
    print(*row)
