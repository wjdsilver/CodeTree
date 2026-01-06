n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=0
active_cols = range(n)

def turn_grid():#회전
    global grid
    new_grid = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            new_grid[b][n-1-a] = grid[a][b]
    grid = new_grid
    

def fall(cols):#해당하는 줄들에 중력 작용
    global tmp
    for j in cols:
        tmp=[]
        for i in range(n):
            if grid[i][j]!=0:
                tmp.append(grid[i][j])
        for i in range(n):
            grid[i][j] = 0
        for k in range(len(tmp)):# 아래부터 채우기
            grid[n-1-k][j] = tmp[-1-k]

def bomb(cols):
    exploded_cols = set()

    for j in cols:
        cnt=1

        for i in range(1,n):
            if grid[i][j] != 0 and grid[i][j] == grid[i-1][j]:#같은 값 연달아 몇개인지 갯수 세기
                cnt+=1
            
            else:
                if cnt>=m:#m개 이상의 같은 숫자가 있는 경우
                    changed = False
                    for k in range(cnt):
                        if grid[i-k-1][j] != 0:
                            grid[i-k-1][j] = 0
                            changed = True
                    if changed:
                        exploded_cols.add(j)
                cnt=1 

        if cnt >= m:
            changed = False
            for k in range(cnt):
                if grid[n-1-k][j] != 0:
                    grid[n-1-k][j] = 0
                    changed = True
            if changed:
                exploded_cols.add(j)
    return exploded_cols                 

for _ in range(k):#터지고 회전하는것을 k번 반복함
    while True:
        cols=bomb(active_cols)#연쇄 폭발
        if not cols:
            break
        fall(cols)
    turn_grid()
    active_cols = range(n)
    fall(active_cols)
while True:#마지막에 한번더 연쇄 폭발
    cols = bomb(range(n))
    if not cols:
        break
    fall(cols)

for row in grid:#남은 폭탄의 수 구하기
    for elem in row:
        if elem!=0:
            ans+=1

print(ans)