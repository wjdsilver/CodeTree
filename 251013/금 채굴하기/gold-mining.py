n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def casek(i, j, k):
    cnt = 0
    for a in range(i - k, i + k + 1):
        for b in range(j - k, j + k + 1):
            if 0 <= a < n and 0 <= b < n:
                if i + j - k <= a + b <= i + j + k:
                    if grid[a][b] == 1:
                        cnt += 1
    if 0 < (cnt * m - (k**2 + (k+1)**2)):
        return cnt
    return 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            ans = max(ans, casek(i, j, k))

print(ans)
