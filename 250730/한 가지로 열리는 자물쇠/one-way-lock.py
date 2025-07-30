N = int(input())
a, b, c = map(int, input().split())

if a<=2:
    a1=0
elif a>2:
    a1=a-3
if N>=a+2:
    a2=a+2
elif N<a+2:
    a2=N

if b<=2:
    b1=0
elif b>2:
    b1=b-3
if N>=b+2:
    b2=b+2
elif N<b+2:
    b2=N

if c<=2:
    c1=0
elif c>2:
    c1=c-3
if N>=c+2:
    c2=c+2
elif N<c+2:
    c2=N

#print(a1,b1,c1)
print(N**3-((N-a2+a1)*(N-b2+b1)*(N-c2+c1)))