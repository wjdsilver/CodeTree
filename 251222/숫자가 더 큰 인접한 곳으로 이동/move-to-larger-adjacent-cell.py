n, curr_x, curr_y = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

# row끼리 입력 받음
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

def inRange(x, y):
    return 0 <= x <= n and 0 <= y <= n

dxs=[-1,1,0,0]
dys=[0,0,-1,1]

print(a[curr_x][curr_y], end=" ")
while True:
    moved = False
    max_num = a[curr_x][curr_y]
    max_x, max_y = curr_x, curr_y

    for dx, dy in zip(dxs, dys):
        nx = curr_x + dx
        ny = curr_y + dy

        if inRange(nx, ny) and a[nx][ny] > max_num:
            max_num = a[nx][ny]
            max_x, max_y = nx, ny
            moved = True
            cnt=1
            print(a[max_x][max_y], end=" ")
            break
            
    if not moved:
        break   # 더 큰 숫자가 없으면 종료

    curr_x, curr_y = max_x, max_y
