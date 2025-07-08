m1, d1, m2, d2 = map(int, input().split())
A=input()
day=[0,31,29,31,30,31,30,31,31,30,31,30,31]
w_day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
def Days(x,y):
    result=0
    for i in range(x):
        result+=day[i]
    result+=y
    return result
w=w_day.index(A)

if Days(m2,d2)-Days(m1,d1)%7>w:
    print((Days(m2,d2)-Days(m1,d1))//7+1)
else:
    print((Days(m2,d2)-Days(m1,d1))//7)


