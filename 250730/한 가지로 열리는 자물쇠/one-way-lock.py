N = int(input())
a, b, c = map(int, input().split())

if a<=2:
    a1=0
elif a>2:
    a1=a-3
if b<=2:
    b1=0
elif b>2:
    b1=b-3
if c<=2:
    c1=0
elif c>2:
    c1=c-3
print(N**3-((N-a-2+a1)*(N-b-2+b1)*(N-c-2+c1)))