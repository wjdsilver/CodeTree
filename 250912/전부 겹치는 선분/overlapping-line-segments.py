n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

L = max(x1)
R = min(x2)

if L <= R:
    print("Yes")
else:
    print("No")