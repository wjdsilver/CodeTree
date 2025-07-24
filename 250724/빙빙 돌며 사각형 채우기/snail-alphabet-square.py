n, m = map(int, input().split())
r,c=0,0
cnt, d=0, 0
num=ord("A")

def inRange(r,c):
    return 0<=r<n and 0<=c<m

arr=[[0]*m for _ in range (n)]
dxs,dys=[0,1,0,-1],[1,0,-1,0]

while cnt < n*m:
    arr[r][c]=chr(num)
    num+=1
    cnt+=1
    if num>ord("Z"):
        num=ord("A")
    nr,nc=r+dxs[d],c+dys[d]
    if not inRange(nr,nc) or arr[nr][nc]!=0:
        d=(d+1)%4
        nr,nc=r+dxs[d],c+dys[d]
    r,c=nr,nc
for row in arr:
    print(*row)
