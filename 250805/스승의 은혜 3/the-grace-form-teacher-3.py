N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]


ans=0

for i in range(N):
    discounted = []
    for j in range(N):
        if i == j:
            discounted.append((gifts[j][0] // 2, gifts[j][1]))
        else:
            discounted.append(gifts[j])
    discounted.sort(key=lambda x:x[0]+x[1])
    cost = [g[0] for g in discounted]
    deliver = [g[1] for g in discounted]

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