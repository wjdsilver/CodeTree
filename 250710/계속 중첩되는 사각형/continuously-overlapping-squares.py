n = int(input())
ans=[[0]*201 for _ in range(201)]
cnt=0

def boxR(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=1

def boxB(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=2

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    if i%2==0:
        boxR(x1+100,y1+100,x2+100,y2+100)
    elif i%2==1:
        boxB(x1+100,y1+100,x2+100,y2+100)

for i in range(201):
    for j in range(201):
        if ans[i][j]==2:
            cnt+=1
print(cnt)