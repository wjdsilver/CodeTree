import sys

arr=list(map(int,input().split()))
big=-sys.maxsize
small=sys.maxsize

for i in arr:
    if i==999 or i==-999:
        break
    if i>big:
        big=i
    if i<small:
        small=i
print(big, small)
