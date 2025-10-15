n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    tmp=u[-1]
    for j in range(n-1,0,-1):
        u[j]=u[j-1]
    u[0]=d[-1]

    for i in range(n-1,0,-1):
        d[i]=d[i-1]
    d[0]=tmp

    
for x in u:
    print(x,end=" ")
print()
for y in d:
    print(y,end=" ")