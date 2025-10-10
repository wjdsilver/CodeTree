n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = []

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < m

# 셀 모양들을 (dx, dy) 오프셋 목록으로 정의
shapes = [
    [(0,0),(0,1),(0,2)],
    [(0,0),(1,0),(2,0)],
    [(0,0),(1,0),(1,1)],
    [(0,0),(1,0),(0,1)],
    [(0,0),(0,1),(1,1)],
    [(0,1),(1,0),(1,1)]
]

for i in range(n):
    for j in range(m):
        for shape in shapes:
            s = 0
            ok = True
            for dx, dy in shape:
                x = i + dx
                y = j + dy
                if not in_bounds(x, y):
                    ok = False
                    break
                s += grid[x][y]
            if ok:
                ans.append(s)

print(max(ans) if ans else 0)
