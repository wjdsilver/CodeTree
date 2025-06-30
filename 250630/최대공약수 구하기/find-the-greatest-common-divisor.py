n, m = map(int, input().split())
div=1
small, big=0, 0
if n>m:
    small=m
    big=n
else:
    small=n
    big=m

for i in range(1,small+1):
    if big%i==0 and small%i==0:
        div=i

print(div)



