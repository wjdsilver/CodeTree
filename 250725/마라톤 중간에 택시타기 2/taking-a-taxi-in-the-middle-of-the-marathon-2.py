import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
min_d=sys.maxsize
total=0

for i in range(1, n):
    total += abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])

for i in range(1, n-1):
    skip = abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])
    skip += abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    shortcut = abs(x[i+1] - x[i-1]) + abs(y[i+1] - y[i-1])
    d = total - skip + shortcut
    min_d = min(min_d, d)

print(min_d)
