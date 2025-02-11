p1=input().split()
p2=input().split()

p1_age=int(p1[0])
p1_gender=p1[1]
p2_age=int(p2[0])
p2_gender=p2[1]

print(int((p1_age>=19 and p1_gender=="M") or (p2_age>=19 and p2_gender=="M")))
