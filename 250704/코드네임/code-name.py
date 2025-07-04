MAX_N = 5
ans=100
mem=0
codes=[]

class Code:
    def __init__(self,name,score):
        self.name=name
        self.score=score

        
for _ in range(MAX_N):
    codename, score = input().split()
    codes.append(Code(codename,int(score)))


for i in range(MAX_N):
    if codes[i].score<ans:
        ans=codes[i].score
        mem=i

print(codes[mem].name,codes[mem].score)


