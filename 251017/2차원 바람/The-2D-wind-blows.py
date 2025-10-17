n, m, q = map(int, input().split()) #행렬 크기 n,m 바람 횟수 q
a = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(map(int, input().split())) for _ in range(q)] #바람 정보 좌상단점, 우하단 점
grid=[[0]*m for _ in range(n)]

def shift(x1,y1,x2,y2):
    x1-=1
    x2-=1
    y1-=1
    y2-=1

    tmp1=a[x1][y2]
    for i in range(y2,y1,-1):
        a[x1][i]=a[x1][i-1]
    
    tmp2=a[x2][y2]
    for i in range(x2,x1+1,-1):
        a[i][y2]=a[i-1][y2]
    a[x1+1][y2]=tmp1

    tmp1=a[x2][y1]
    for i in range(y1,y2-1):
        a[x2][i]=a[x2][i+1]
    a[x2][y2-1]=tmp2

    for i in range(x1,x2-1):
        a[i][y1]=a[i+1][y1]
    a[x2-1][y1]=tmp1

def returnAve(i,j):
    cnt=1
    total=a[i][j]
    if 0<=i-1<n:
        total+=a[i-1][j]
        cnt+=1
    if 0<=i+1<n:
        total+=a[i+1][j]
        cnt+=1
    if 0<=j-1<m:
        total+=a[i][j-1]
        cnt+=1
    if 0<=j+1<m:
        total+=a[i][j+1]
        cnt+=1
    return total//cnt

def average(x1,y1,x2,y2):
    x1-=1
    x2-=1
    y1-=1
    y2-=1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            grid[i-x1][j-y1]=returnAve(i,j)

for j in range(q):
    shift(winds[j][0],winds[j][1],winds[j][2],winds[j][3])
    average(winds[j][0],winds[j][1],winds[j][2],winds[j][3])
    for k in range(winds[j][0]-1,winds[j][2]):
        for l in range(winds[j][1]-1,winds[j][3]):
            a[k][l]=grid[k-winds[j][0]+1][l-winds[j][1]+1]

for row in a:
    print(*row)
    