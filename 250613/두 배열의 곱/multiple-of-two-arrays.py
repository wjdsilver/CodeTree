arr1_2d = [
	list(map(int, input().split()))
	for _ in range(3)
]
input()
arr2_2d = [
	list(map(int, input().split()))
	for _ in range(3)
]

for i in range(3):
    for j in range(3):
        print(arr1_2d[i][j]*arr2_2d[i][j],end=" ")
    print()