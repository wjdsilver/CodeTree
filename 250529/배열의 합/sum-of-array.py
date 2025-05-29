n = 4
arr_2d = []
for _ in range(n):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for i in range(n):
    ans=0
    for j in range(n):
        ans+=arr_2d[i][j]
    print(ans)