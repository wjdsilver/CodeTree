n, k = map(int, input().split())
arr = list(map(int, input().split()))
fin=max(arr)

for i in range(min(arr),max(arr)):#최소
    cost=0
    for x in arr:
        if x<i:
            cost+=(i-x)
        if x>(i+k):
            cost+=(x-i-k)
    fin=min(fin,cost)
print(fin)
