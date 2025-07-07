n = int(input())
score=[]

class Score:
    def __init__(self,name,s1,s2,s3):
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3

for _ in range(n):
    name,s1,s2,s3 = input().split()
    score.append(Score(name,int(s1),int(s2),int(s3)))

score.sort(key=lambda x:x.s1+x.s2+x.s3)
for elem in score:
    print(elem.name, elem.s1, elem.s2, elem.s3)