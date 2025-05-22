import sys

arr=list(map(int,input().split()))
n=-sys.maxsize
for i in arr:
    if i>n:
        n=i
print(n)