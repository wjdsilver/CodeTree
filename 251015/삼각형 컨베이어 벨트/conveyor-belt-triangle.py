n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    tmp=l[-1]
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    l[0]=d[n-1]
    
    tmp1=r[n-1]
    for j in range(n-1,0,-1):
        r[j]=r[j-1]
    r[0]=tmp

    for k in range(n-1,0,-1):
        d[k]=d[k-1]
    d[0]=tmp1
print(*l)
print(*r)
print(*d)

    