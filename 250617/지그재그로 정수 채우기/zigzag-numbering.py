n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            arr_2d[i][j] = n*j+i
        else:
            arr_2d[i][j] = n*j+(n-i)-1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()
