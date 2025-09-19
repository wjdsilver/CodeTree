a, b, x, y = map(int, input().split())

case1=abs(a-x)+abs(b-y)
case2=abs(a-y)+abs(b-x)
print(min(case1,case2,abs(a-b)))