n = 5
arr_2d = []
for _ in range(n):
    arr_1d =input().split()
    arr_2d.append(arr_1d)

for i in range(n):
    for j in range(3):
        print(chr(ord(arr_2d[i][j])-32),end=" ")
    print()