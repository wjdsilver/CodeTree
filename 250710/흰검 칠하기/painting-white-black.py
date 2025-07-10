n = int(input())
WHITE, BLACK, GRAY = 1, 2, 3
size = 200001
offset = 100000

# 각 색 횟수 카운트 배열
white = [0] * size
black = [0] * size
color = [0] * size  # 현재 타일 상태 (1=흰, 2=검, 3=회)

cur = offset

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == "L":
        for i in range(cur, cur - x, -1):
            if color[i] == GRAY:
                continue
            white[i] += 1
            if white[i] >= 2 and black[i] >= 2:
                color[i] = GRAY
            elif color[i] != BLACK:
                color[i] = WHITE
        cur = cur - x
    else:  # "R"
        for i in range(cur, cur + x):
            if color[i] == GRAY:
                continue
            black[i] += 1
            if white[i] >= 2 and black[i] >= 2:
                color[i] = GRAY
            elif color[i] != WHITE:
                color[i] = BLACK
        cur = cur + x - 1

# 최종 색상 카운트
w = color.count(WHITE)
b = color.count(BLACK)
g = color.count(GRAY)

print(w, b, g)
