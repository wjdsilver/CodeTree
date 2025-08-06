import sys
n = int(input())
a = list(map(int, input().split()))

fin=sys.maxsize
for i in range(min(a)+1,max(a)):
    fin=min(i//2,fin)
print(fin)