n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    cnt = 1
    clist = []
    for j in range(1, n):
        if grid[i][j-1] == grid[i][j]:
            cnt += 1
        else:
            clist.append(cnt)
            cnt = 1
    clist.append(cnt)  # 마지막 구간 추가
    if max(clist) >= m:
        ans += 1

for i in range(n):
    cnt = 1
    clist = []
    for j in range(1, n):
        if grid[j-1][i] == grid[j][i]:
            cnt += 1
        else:
            clist.append(cnt)
            cnt = 1
    clist.append(cnt)
    if max(clist) >= m:
        ans += 1

print(ans)
