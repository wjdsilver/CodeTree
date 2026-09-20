n = int(input())
segments = []
answer=0

for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))
segments.sort()

def dfs(idx, last_end, count):
    global answer

    if idx == n:
        answer = max(answer, count)
        return

    start, end = segments[idx]

    # 선택하지 않음
    dfs(idx + 1, last_end, count)

    # 선택함
    if start > last_end:
        dfs(idx + 1, end, count + 1)

dfs(0,0,0)
print(answer)
