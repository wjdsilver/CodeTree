n=int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]
if n%2==0:
    for i in range(n):
        for j in range(n):
            if j%2==1:
                arr_2d[i][j] = (n-j)*n-i
            else:
                arr_2d[i][j] = (n-j-1)*n+i+1
else:
    for i in range(n):
        for j in range(n):
            if j%2==0:
                arr_2d[i][j] = (n-j)*n-i
            else:
                arr_2d[i][j] = (n-j-1)*n+i+1

                
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()


