def Count(d,t,m):
    result=0
    result+=d*24*60
    result+=t*60
    result+=m
    return result

a, b, c = map(int, input().split())
if Count(a,b,c)-Count(11,11,11)>0:
    print(Count(a,b,c)-Count(11,11,11))
else:
    print("-1")