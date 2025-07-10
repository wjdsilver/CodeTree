ans = [[0]*2001 for _ in range(2001)]
cnt=0
maxX,maxY=-1,-1
minX,minY=2001,2001

def box1(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=1

def box0(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=0

x1,y1,x2,y2 = map(int,input().split())
box1(x1+1000,y1+1000,x2+1000,y2+1000)
x1,y1,x2,y2 = map(int,input().split())
box0(x1+1000,y1+1000,x2+1000,y2+1000)

for i in range(2001):
    for j in range(2001):
        if ans[i][j]==1:
            maxX = max(maxX, i)
            minX = min(minX, i)
            maxY = max(maxY, j)
            minY = min(minY, j)
if maxX == -1:
    print(0)
elif maxY == -1:
    print(0)
else:
    print((maxX-minX+1)*(maxY-minY+1))