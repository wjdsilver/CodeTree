n = int(input())
curr_x, curr_y = map(int, input().split())

grid = [["."] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = input()
    for j in range(1, n + 1):
        grid[i][j] = row[j - 1]

dxs=[0,-1,0,1]
dys=[1,0,-1,0]
dirr=0
ingrid=True
time=1
visited = [[[False]*4 for _ in range(n+1)] for _ in range(n+1)]

def inRange(x,y):
    return 1 <= x <= n and 1 <= y <= n

def turn(x, y):
    global dirr, time, ingrid

    if visited[x][y][dirr]:
        print(-1)
        exit()

    visited[x][y][dirr] = True
    
    # 1. 앞칸
    nx = x + dxs[dirr]
    ny = y + dys[dirr]
    

    # 격자 탈출
    if not inRange(nx, ny):
        ingrid = False
        return x, y

    # 2. 앞이 벽이면 반시계 회전
    if grid[nx][ny] == "#":
        dirr = (dirr + 1) % 4
        return x, y

    # 3. 이동 가능한 경우
    # 오른쪽 확인 (시계 방향)
    right = (dirr + 3) % 4
    rx = nx + dxs[right]
    ry = ny + dys[right]

    # 이동
    x, y = nx, ny
    time+=1


    # 오른쪽이 비어 있으면 방향 전환
    if inRange(rx, ry) and grid[rx][ry] == ".":
        dirr = right

    return x, y


        
while ingrid==True:
    curr_x, curr_y = turn(curr_x, curr_y)
print(time)