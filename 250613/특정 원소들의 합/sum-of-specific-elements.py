n = 4
arr_2d = []
ans=0
for _ in range(n):
    arr_1d =list(map(int,input().split()))
    arr_2d.append(arr_1d)

for i in range(n):
    for j in range(4):
        if i>=j:
            ans+=arr_2d[i][j]
print(ans)