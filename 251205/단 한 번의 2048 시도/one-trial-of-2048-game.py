def right():
    for i in range(4):
        row = [v for v in grid[i] if v != 0] 
        row = [0] * (4 - len(row)) + row
        for j in range(3, 0, -1):
            if row[j] == row[j - 1] and row[j] != 0:
                row[j] *= 2
                row[j - 1] = 0
        row = [v for v in row if v != 0]
        row = [0] * (4 - len(row)) + row
        grid[i]=row

def left():
    for i in range(4):
        row = [v for v in grid[i] if v != 0]
        row = row + [0] * (4 - len(row))
        for j in range(3):
            if row[j] == row[j + 1] and row[j] != 0:
                row[j] *= 2
                row[j + 1] = 0
        row = [v for v in row if v != 0]
        row = row + [0] * (4 - len(row))
        grid[i]=row

def up():
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        col = [v for v in col if v != 0] + [0] * (4 - len([v for v in col if v != 0]))
        for i in range(3):
            if col[i] == col[i+1] and col[i] != 0:
                col[i] *= 2
                col[i+1] = 0
        col = [v for v in col if v != 0] + [0] * (4 - len([v for v in col if v != 0]))
        for i in range(4):
            grid[i][j] = col[i]

def down():
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        col = [v for v in col if v != 0]
        col = [0] * (4 - len(col)) + col
        for i in range(3, 0, -1):
            if col[i] == col[i - 1] and col[i] != 0:
                col[i] *= 2
                col[i - 1] = 0
        col = [v for v in col if v != 0]
        col = [0] * (4 - len(col)) + col
        for i in range(4):
            grid[i][j] = col[i]

grid = [list(map(int, input().split())) for _ in range(4)]

dir = input()
if dir=="L":
    left()
elif dir=="R":
    right()
elif dir=="U":
    up()
elif dir=="D":
    down()

for elem in grid:
    print(*elem)