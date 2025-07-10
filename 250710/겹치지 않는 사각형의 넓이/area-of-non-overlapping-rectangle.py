x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

ans=[[0]*2001 for _ in range(2001)]
cnt=0

def box(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=1
def m(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=0

for i in range(2):
    box(x1[i],y1[i],x2[i],y2[i])
m(x1[2],y1[2],x2[2],y2[2])

for i in range(2001):
    for j in range(2001):
        if ans[i][j]==1:
            cnt+=1
print(cnt)