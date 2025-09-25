n = int(input())
a = list(map(int, input().split()))
small=100

for i in range(n):
    if a[i]>min(a) and small>a[i]:
        small=a[i]

if small==100 or a.count(small)>1:
    print(-1)
else:
    print(a.index(small)+1)

