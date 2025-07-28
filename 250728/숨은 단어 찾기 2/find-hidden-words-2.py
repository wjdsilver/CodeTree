N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cnt=0

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j]=="L":
            for m in range(8):
                x1, y1 = i + dxs[m], j + dys[m]
                x2, y2 = i + dxs[m] * 2, j + dys[m] * 2
                if in_range(x1, y1) and in_range(x2, y2):
                    if arr[x1][y1] == "E" and arr[x2][y2] == "E":
                        cnt += 1
print(cnt)
