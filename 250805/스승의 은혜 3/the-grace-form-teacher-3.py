N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts.sort()

ans=0

for i in range(N):
    cost = [g[0] for g in gifts]
    deliver = [g[1] for g in gifts]
    cost[i] //= 2

    total = 0
    count = 0
    for j in range (len(cost)):
        if total + cost[j] +deliver[j] <= B:
            total = total +cost[j] +deliver[j]
            count += 1
        else:
            break
    ans = max(ans, count)
if ans!=0:
    print(ans)
else:
    print(1)