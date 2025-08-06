N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
ans=0

for t in range(1,1001):
    effort=0
    for i in range(N):
        if t<ranges[i][0]:
            effort+=C
        elif ranges[i][0]<=t<=ranges[i][1]:
            effort+=G
        elif ranges[i][1]<t:
            effort+=H
    ans=max(ans,effort)
print(ans)