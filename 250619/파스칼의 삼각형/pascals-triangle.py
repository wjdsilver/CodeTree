n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

arr_2d[0][0]=1
arr_2d[1][0]=1
arr_2d[1][1]=1

for i in range (2,n):
    for j in range(n):
        arr_2d[i][j] = arr_2d[i-1][j-1] +arr_2d[i-1][j] 


for i in range(n):
	for j in range(i + 1):
		print(arr_2d[i][j], end=" ")
	print()


