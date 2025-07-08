m1, d1, m2, d2 = map(int, input().split())

day=[31,28,31,30,31,30,31,31,30,31,30,31]
w_day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
def Days(x,y):
    result=0
    for i in range(x):
        result+=day[i]
    result+=y
    return result

w=(Days(m2,d2)-Days(m1,d1))%7
print(w_day[w])

