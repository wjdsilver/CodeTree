import sys

n = int(input())
arr = list(map(int, input().split()))
end=n

while True:
    big = -sys.maxsize 
    idx = 0

    for i in range(end):
        if arr[i] > big:
            big = arr[i]
            idx = i

    print(idx + 1,end=" ")

    if idx + 1 == 1: 
        break
    end = idx

