a, b = map(int, input().split())

def pro(a,b):
    if a>b:
        a=a+25
        b=b*2
    else:
        a=a*2
        b=b+25
    return (a,b)

a,b=pro(a,b)
print(a,b)