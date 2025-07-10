n = int(input())
x1, y1, x2, y2 = [], [], [], []
ans=[[0]*2001 for _ in range(2001)]
cnt=0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)

def box(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            ans[i][j]=1

for i in range(n):
    box(x1[i],y1[i],x2[i],y2[i])

for i in range(2001):
    for j in range(2001):
        if ans[i][j]==1:
            cnt+=1
print(cnt)

