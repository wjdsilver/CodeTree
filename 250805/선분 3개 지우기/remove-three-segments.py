n = int(input())
nLine=[]
for _ in range(n):
    left, right = map(int, input().split())
    nLine.append((left,right))
ans=0

for i in range(len(nLine)):
    for j in range(i+1,len(nLine)):
        for k in range(j+1,len(nLine)):
            line=[0]*101
            valid=True
            for idx in range(n):
                if idx == i or idx == j or idx == k:
                    continue
                for m in range(nLine[idx][0],nLine[idx][1]+1):
                    line[m]+=1
                    if line[m]>=2:
                        valid=False
                        break
                if not valid:
                    break
            if valid:
                ans+=1

print(ans)
                
                    
