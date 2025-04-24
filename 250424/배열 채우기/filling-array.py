arr = list(map(int, input().split()))
n=len(arr)
if arr[n-1]==0:
    arr.pop()
    for i in range(0,n-1):
        print(arr.pop(),end=" ")
else:
    for i in range(0,n):
        print(arr.pop(),end=" ")

