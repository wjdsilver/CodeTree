n = 5
info=[]

class Info:
    def __init__(self,name,h,w):
        self.name=name
        self.h=h
        self.w=w

for _ in range(n):
    n, h, w = input().split()
    info.append(Info(n,int(h),float(w)))

info.sort(key=lambda x:x.name)
print("name")
for elem in info:
    print(elem.name,elem.h,elem.w)
print()
info.sort(key=lambda x:-x.h)
print("height")
for elem in info:
    print(elem.name,elem.h,elem.w)  

