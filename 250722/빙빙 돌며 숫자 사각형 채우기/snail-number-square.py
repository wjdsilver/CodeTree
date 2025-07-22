n, m = map(int, input().split())
answer = [
    [0] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0           # 시작은 (0, 0)
dir_num = 0           # 0: 오른쪽, 1: 아래쪽, 2: 위쪽

answer[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 시계방향으로 90 회전
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num+1)%4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

    x, y = nx,ny
    answer[x][y] = i


for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()
