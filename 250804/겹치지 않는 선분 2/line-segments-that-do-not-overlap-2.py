n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
cnt=0

for i in range(n):
    x1, y1 = lines[i]
    inter= False
    for j in range(n):
        if i == j:
            continue
        x2, y2 = lines[j]
        if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            inter = True
            break
    if not inter:
        cnt += 1

print(cnt)