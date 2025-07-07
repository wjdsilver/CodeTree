n = int(input())
students = []

class Student:
    def __init__(self,height,weight,num):
        self.height=height
        self.weight=weight
        self.num=num

for i in range(n):
    h,w=input().split()
    students.append(Student(int(h),int(w),i+1))

students.sort(key=lambda x:(-x.height,-x.weight,x.num))
for elem in students:
    print(elem.height, elem.weight, elem.num)
