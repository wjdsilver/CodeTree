a, b, c = map(int, input().split())


def Count(d,t,m):
    result=0
    result+=d*24*60
    result+=t*60
    result+=m
    return result

print(Count(a,b,c)-Count(11,11,11))