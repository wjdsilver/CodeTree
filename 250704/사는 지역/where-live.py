n = int(input())
name = []
street_address = []
region = []
information=[]

class Info:
    def __init__(self,name,num,place):
        self.name=name
        self.num=num
        self.place=place

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)
    information.append(Info(n_i,s_i,r_i))

name.sort()

for i in range(n):
    if information[i].name==name[n-1]:
        print(f"""name {information[i].name}
addr {information[i].num}
city {information[i].place}""")



        