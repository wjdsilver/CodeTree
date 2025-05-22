import sys

n = int(input())
arr = list(map(int, input().split()))
cnt=0

small=sys.maxsize
for i in arr:
    if i<small:
        small=i
for i in arr:
    if i==small:
        cnt+=1
print(small, cnt)
