n,m=map(int,input().split())

arr1_2d = [
	list(map(int, input().split()))
	for _ in range(n)
]

arr2_2d = [
	list(map(int, input().split()))
	for _ in range(n)
]

arr3_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
	for j in range(m):
		if arr1_2d[i][j]==arr2_2d[i][j]:
			arr3_2d[i][j]=0
		else:
			arr3_2d[i][j]=1

for row in arr3_2d:
    for elem in row:
        print(elem, end=" ")
    print()