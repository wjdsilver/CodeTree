a = list(map(int, input().split()))
a.sort()
s=a[0]
m=a[1]
l=a[2]
print(max(l-m-1,m-s-1))