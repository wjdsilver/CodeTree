n, m, q = map(int, input().split())#행렬크기 n,m ,바람 횟수 q
grid = [list(map(int, input().split())) for _ in range(n)]
wind= [(int(r)-1, d) for r, d in [input().split() for _ in range(q)]]#바람 부는 줄, 바람 방향 

def Rwind(l):#왼쪽으로
    tmp=grid[l][0]
    for i in range(m-1):
        grid[l][i]=grid[l][i+1]
    grid[l][m-1]=tmp

def Lwind(l):#오른쪽으로
    tmp=grid[l][-1]
    for j in range(m-1,0,-1):
        grid[l][j]=grid[l][j-1]
    grid[l][0]=tmp

def same(l1,l2):
    for k in range(m):
        if grid[l1][k] == grid[l2][k]:
            return True
    return False

for w in range(q):#총 q번의 바람이 불어옴
    up=wind[w][0]-1
    down=wind[w][0]+1
    way=wind[w][1]

    if way=="R":
        Rwind(wind[w][0])
        way="L"
    elif way=="L":
        Lwind(wind[w][0])
        way="R"
    
    while up>=0 and same(up+1,up)==True:
        if way=="R":
            Rwind(up)
            way="L"
            up-=1
        elif way=="L":
            Lwind(up)
            way="R"
            up-=1

    way=wind[w][1]#위쪽의 마지막 바람 방향으로 way가 설정되어있으므로 재참조
    if way=="R":
        way="L"
    elif way=="L":
        way="R"

    while down<n and same(down,down-1)==True:
        if way=="R":
            Rwind(down)
            way="L"
            down+=1
        elif way=="L":
            Lwind(down)
            way="R"
            down+=1
for row in grid:
    print(*row)