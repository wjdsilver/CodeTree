n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=-1

def positive(x1,y1,x2,y2):
    numpos=True
    cnt=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if grid[i][j]<0:
                numpos=False
            else:
                cnt+=1
    if numpos==True:
        return cnt
    else:
        return -1
        

for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1,n):
            for y2 in range(y1,m):
                ans=max(ans,positive(x1,y1,x2,y2))
print(ans)
