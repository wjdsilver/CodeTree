N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

ans=0

for i in range(N):
    cost = P[:]
    cost[i] //= 2

    total = 0
    count = 0
    for j in range (len(cost)):
        if total + cost[j] +S[j] <= B:
            total = total +cost[j] +S[j]
            count += 1
        else:
            break
    ans = max(ans, count)
if ans!=0:
    print(ans)
else:
    print(1)