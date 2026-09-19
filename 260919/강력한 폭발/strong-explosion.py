N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

bombs = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            bombs.append((i, j))

vertical = [
    (-2, 0),
    (-1, 0),
    (0, 0),
    (1, 0),
    (2, 0)
]
cross = [
    (-1, 0),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, 0)
]
xshape = [
    (-1, -1),
    (-1, 1),
    (0, 0),
    (1, -1),
    (1, 1)
]
shapes = [vertical, cross, xshape]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

destroyed = [[False] * N for _ in range(N)]

answer = 0

def dfs(idx, count):
    global answer

    # 모든 폭탄에 종류를 정했다면
    if idx == len(bombs):
        answer = max(answer, count)
        return

    x, y = bombs[idx]

    for shape in shapes:

        added = []

        # 현재 폭탄이 초토화시키는 칸 확인
        for dx, dy in shape:
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and not destroyed[nx][ny]:
                destroyed[nx][ny] = True
                added.append((nx, ny))

        # 다음 폭탄으로
        dfs(idx + 1, count + len(added))

        # 원상복구
        for nx, ny in added:
            destroyed[nx][ny] = False


dfs(0, 0)

print(answer)


