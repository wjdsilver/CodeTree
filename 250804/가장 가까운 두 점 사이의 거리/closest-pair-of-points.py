import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
ans=sys.maxsize

for i in range (n-1):
    for j in range(i+1,n):
        result=((abs(x[i]-x[j]))**2+(abs(y[i]-y[j]))**2)
    ans=min(ans,result)
print(ans)