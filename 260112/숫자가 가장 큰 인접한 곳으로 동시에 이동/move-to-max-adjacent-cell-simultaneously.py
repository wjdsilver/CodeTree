n, m, t = map(int, input().split())
#격자판 정보
a = [list(map(int, input().split())) for _ in range(n)]
balls = [[0]*n for _ in range(n)]
tmp = [[0]*n for _ in range(n)]

# 구슬 위치
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]
#상하좌우
dxs=[-1,1,0,0]
dys=[0,0,-1,1]

#입력받은 구슬 위치를 좌표로 바꾸어서 저장
for x, y in marbles:
    balls[x-1][y-1] = 1

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def where2move(x, y):
    best_x, best_y = x, y
    best_value = 0

    for d in range(4):
        nx = x + dxs[d]
        ny = y + dys[d]
        if inRange(nx, ny) and a[nx][ny] > best_value:
            best_value = a[nx][ny]
            best_x, best_y = nx, ny

    if best_x == x and best_y == y:
        return

    if tmp[best_x][best_y] == 0:
        tmp[best_x][best_y] = 1
    elif tmp[best_x][best_y] == 1:
        tmp[best_x][best_y] = -1


for _ in range(t):
    tmp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if balls[i][j] == 1:
                where2move(i, j)

    for i in range(n):
        for j in range(n):
            balls[i][j] = 1 if tmp[i][j] == 1 else 0


ans = 0
for i in range(n):
    for j in range(n):
        if balls[i][j] == 1:
            ans += 1
print(ans)

#입력된 구슬 위치를 바탕으로 balls 작성.
#balls에서 구슬이 있는 위치에 대해서 a값을 확인, balls에 구슬 위치 정보 변경
