n=int(input())
ans = [[0]*201 for _ in range(201)]
cnt=0


def box(a,b):
    for i in range(a,a+8):
        for j in range(b,b+8):
            ans[i][j]=1

for i in range(n):
    x, y = map(int,input().split())
    box(x,y)

for i in range(201):
    for j in range(201):
        if ans[i][j]==1:
            cnt+=1
print(cnt)