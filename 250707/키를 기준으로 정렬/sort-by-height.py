n = int(input())
people=[]

class Info():
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

for _ in range(n):
    n_i, h_i, w_i = input().split()
    people.append(Info(n_i,int(h_i),int(w_i)))

people.sort(key=lambda x:x.height)
for elem in people:
    print (elem.name, elem.height, elem.weight)

