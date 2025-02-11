num=input().split()
a=int(num[0])
b=int(num[1])
c=int(num[2])

if a>=b and a>=c:
    print(a)
elif b>=c and b>=a:
    print(b)
elif c>=a and c>=b:
    print(c)