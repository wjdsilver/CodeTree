a, b, c, d = map(int, input().split())

def Time(x,y):
    time=60*x+y
    return time

print(Time(c,d)-Time(a,b))