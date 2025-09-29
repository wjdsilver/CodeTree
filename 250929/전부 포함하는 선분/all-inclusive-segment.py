n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
ans=100

for i in range(n):
    remain = segments[:i] + segments[i+1:]
    # 왼쪽 끝점 중 최소, 오른쪽 끝점 중 최대
    m = min(seg[0] for seg in remain)
    M = max(seg[1] for seg in remain)
    ans=min(ans,M-m)
print(ans)