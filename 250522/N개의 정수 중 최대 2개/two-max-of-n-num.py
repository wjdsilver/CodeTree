import sys

n = int(input())
a = list(map(int, input().split()))
arr=[]
for _ in range(n):
    big=-sys.maxsize
    for i in a:
        if i>big:
            big=i
    arr.append(big)
    a.remove(big)
print(arr[0],arr[1])
