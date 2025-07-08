n = int(input())
students = []

class Info:
    def __init__(self,h,w,no):
        self.h=h
        self.w=w
        self.no=no

for i in range(n):
    h,w=map(int,input().split())
    students.append(Info(h,w,i+1))

students.sort(key=lambda x:(x.h,-x.w))
for elem in students:
    print(elem.h,elem.w,elem.no)