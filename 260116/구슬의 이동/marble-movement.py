# 각자의 속도로 이동, 벽 부딪히면 방향 전환, 방향 전환에는 시간 소요 안됨
# 정수시간에 같은 칸에 K개 이하면 전부 생존, K개 이상이면 우선 순위 높은거부터 생존. 
# 우선순위는 1. 속도가 빠른거 2. 구슬의 번호가 더 큰거 
def inRange(x,y,n):
    return 0<=x<n and 0<=y<n

def test():
    for _ in range(m):
        xi, yi, di, vi = input().split()
        x.append(int(xi) - 1)
        y.append(int(yi) - 1)
        v.append(int(vi))

        if di == "U":
            dr.append(-1); dc.append(0)
        elif di == "D":
            dr.append(1); dc.append(0)
        elif di == "L":
            dr.append(0); dc.append(-1)
        elif di == "R":
            dr.append(0); dc.append(1)

    grid = [[[] for _ in range(n)] for _ in range(n)]    

    #M개의 구슬에 대하여
    for i in range(m):
        grid[x[i]][y[i]].append(i) #몇번째 구슬이 해당 위치에 있는지
    for _ in range(t):
        newgrid = [[[] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for idx in grid[i][j]:
                    r, c = i, j

                    # 속도만큼 이동
                    for _ in range(v[idx]):
                        nr = r + dr[idx]
                        nc = c + dc[idx]

                        if not inRange(nr, nc, n):
                            dr[idx] *= -1
                            dc[idx] *= -1
                            nr = r + dr[idx]
                            nc = c + dc[idx]

                        r, c = nr, nc

                    newgrid[r][c].append(idx)

        # 충돌 처리 (k개 초과 시 우선순위)
        for i in range(n):
            for j in range(n):
                if len(newgrid[i][j]) > k:
                    newgrid[i][j].sort(
                        key=lambda idx: (v[idx], idx),
                        reverse=True
                    )
                    newgrid[i][j] = newgrid[i][j][:k]

        grid = newgrid

    # 구슬 세기
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += len(grid[i][j])

    return ans


n, m, t, k = map(int, input().split())
x, y, v, dr, dc = [], [], [], [], [] #r과 c는 d인풋을 바탕으로 이동하는 방향에 따른 위치 저장한거
    
print(test())