N=input()
x,y=0,0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num=3
for i in range(len(N)):
    d=N[i]
    if d=="L":
        dir_num = (dir_num - 1 + 4) % 4
    elif d=="R":
        dir_num = (dir_num + 1) % 4
    elif d=="F":
        x, y = x + dx[dir_num], y + dy[dir_num]
print(x,y)