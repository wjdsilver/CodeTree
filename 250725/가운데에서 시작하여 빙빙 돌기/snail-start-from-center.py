import sys
n = int(input())
grid = [[0] * n for _ in range(n)]

r,c=n//2,n//2
cnt, step=1, 1
grid[r][c]=cnt

def inRange(r,c):
    return 0<=r<n and 0<=c<n

dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]
d = 0 

while cnt < n*n:
    for _ in range(2):  # 두 번씩 반복
        for _ in range(step):
            r += dxs[d]
            c += dys[d]
            cnt += 1
            grid[r][c] = cnt
            if cnt==n*n:
                for row in grid:
                    print(*row)
                sys.exit() 
        d = (d + 1) % 4 
    step += 1
        

