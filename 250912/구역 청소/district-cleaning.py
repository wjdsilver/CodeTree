a, b = map(int, input().split())
c, d = map(int, input().split())

start=min(a,c)
finish=max(b,d)

if b<c and a<d:
    ans=b+d-a-c
elif b>c and a>d:
    ans=b+d-a-c
else:
    ans=finish-start
print(ans)