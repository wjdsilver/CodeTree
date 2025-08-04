n, B = map(int, input().split())
P = [int(input()) for _ in range(n)]
P.sort()
ans=0

for i in range(n):
    cost = P[:]
    cost[i] //= 2
    cost.sort()

    total = 0
    count = 0
    for price in cost:
        if total + price <= B:
            total += price
            count += 1
        else:
            break
    ans = max(ans, count)

print(ans)