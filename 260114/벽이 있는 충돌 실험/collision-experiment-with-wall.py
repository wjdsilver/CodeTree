T = int(input())

def inRange(x,y,n):
    return 0<=x<n and 0<=y<n

def test():
    n, m = map(int, input().split())
    x, y, r, c = [], [], [], []
    grid=[[0]*n for _ in range(n)]
    for _ in range(m):
        xi, yi, di = input().split()
        x.append(int(xi)-1)
        y.append(int(yi)-1)
        if di=="U":
            r.append(-1)
            c.append(0)
        elif di=="D":
            r.append(1)
            c.append(0) 
        elif di=="L":
            r.append(0)
            c.append(-1)
        elif di=="R":
            r.append(0)
            c.append(1)
    
    #M개의 구슬에 대하여
    for i in range(m):
        grid[x[i]][y[i]]=i+1#몇번째 구슬인지
    for _ in range(2*n):
        newgrid=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    idx = grid[i][j] - 1

                    ni = i + r[idx] 
                    nj = j + c[idx]


                    if not inRange(ni, nj, n):
                        r[idx] *= -1
                        c[idx] *= -1
                        if newgrid[i][j] == 0:
                            newgrid[i][j] = grid[i][j]
                        else:
                            newgrid[i][j] = 0
                    else:
                        if newgrid[ni][nj] == 0:
                            newgrid[ni][nj] = grid[i][j]
                        else:
                            newgrid[ni][nj] = 0
    
        grid = newgrid
    cnt=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]!=0:
                cnt+=1
    return cnt



#T번의 시뮬레이션을 진행함
for _ in range(T):
    print(test())
