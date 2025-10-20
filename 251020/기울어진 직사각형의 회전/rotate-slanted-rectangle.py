n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r -= 1
c -= 1


def get_diamond_path(r, c, m1, m2, m3, m4):
    path = []
    x, y = r, c

    for _ in range(m1):
        path.append((x, y))
        x, y = x - 1, y + 1

    for _ in range(m2):
        path.append((x, y))
        x, y = x - 1, y - 1

    for _ in range(m3):
        path.append((x, y))
        x, y = x + 1, y - 1

    for _ in range(m4):
        path.append((x, y))
        x, y = x + 1, y + 1  

    return path


def clock(r, c):
    path = get_diamond_path(r, c, m1, m2, m3, m4)
    values = [grid[px][py] for px, py in path]
    rotated_values = values[1:] + [values[0]]

    for i in range(len(path)):
        px, py = path[i]
        grid[px][py] = rotated_values[i]


def anticlock(r, c):
    path = get_diamond_path(r, c, m1, m2, m3, m4)
    values = [grid[px][py] for px, py in path]
    rotated_values = [values[-1]] + values[:-1]

    for i in range(len(path)):
        px, py = path[i]
        grid[px][py] = rotated_values[i]


if dir == 0:

    anticlock(r, c)

elif dir == 1:

    clock(r, c)

for row in grid:

    print(*row)