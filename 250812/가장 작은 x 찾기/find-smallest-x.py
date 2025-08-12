n = int(input())

ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
ans=0

for x in range(1,b[0]+1):
    double=False
    temp=x
    for i in range(0,n):
        if a[i]<=x*2<=b[i]:
            x*=2
            double=True
        else:
            double=False
            break
    if double==True:
        if ans==0:
            ans=temp
            print(ans)
            break