import sys

n = int(input())
arr = list(map(int, input().split()))
small=sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        gap=arr[j]-arr[i]
        if gap < small:
            small = gap
print(small)

