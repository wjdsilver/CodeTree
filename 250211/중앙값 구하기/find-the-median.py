num=input().split()
a=int(num[0])
b=int(num[1])
c=int(num[2])

if a>b and a>c:
    if b>c:
        print(b)
    else:
        print(c)
elif b>a and b>c:
    if a>c:
        print(a)
    else:
        print(c)
elif c>a and c>b:
    if a>b:
        print(a)
    else:
        print(b)