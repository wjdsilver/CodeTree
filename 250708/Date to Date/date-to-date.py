m1, d1, m2, d2 = map(int, input().split())

day=[31,28,31,30,31,30,31,31,30,31,30,31]

def Days(x,y):
    result=0
    for i in range(x):
        result+=day[i]
    result+=y
    return result

print(Days(m2,d2)-Days(m1,d1))
