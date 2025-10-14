n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
fin = [0]

def square(i, j, a, b):
    total = grid[i][j]
    x, y = i, j
    # ↘ 방향으로 a칸
    for _ in range(a):
        x += 1; y += 1
        if not (0 <= x < n and 0 <= y < n): return 0
        total += grid[x][y]
    # ↙ 방향으로 b칸
    for _ in range(b):
        x += 1; y -= 1
        if not (0 <= x < n and 0 <= y < n): return 0
        total += grid[x][y]
    # ↖ 방향으로 a칸
    for _ in range(a):
        x -= 1; y -= 1
        if not (0 <= x < n and 0 <= y < n): return 0
        total += grid[x][y]
    # ↗ 방향으로 b칸
    for _ in range(b-1):
        x -= 1; y += 1
        if not (0 <= x < n and 0 <= y < n): return 0
        total += grid[x][y]
    return total

for i in range(n):
    for j in range(n):
        for a in range(1, n):
            for b in range(1, n):
                fin.append(square(i, j, a, b))

print(max(fin))