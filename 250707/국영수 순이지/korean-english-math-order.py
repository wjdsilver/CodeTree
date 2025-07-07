n = int(input())
score=[]

class Score:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

for _ in range(n):
    n_i,k_i,e_i,m_i = input().split()
    score.append(Score(n_i,int(k_i),int(e_i),int(m_i)))

score.sort(key=lambda x:(-x.kor,-x.eng,-x.math))
for elem in score:
    print (elem.name,elem.kor,elem.eng,elem.math)


  