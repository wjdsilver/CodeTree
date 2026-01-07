n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=0

def inRange(x,y):
    return 0<=x<n and 0<=y<n

#tmp grid의 해당 칸에 대해서 폭발 진행
def bomb(i,j):
    global tmp_grid,row_start,row_end,col_start,col_end
    pick=grid[i][j]#고른 칸에 적혀 있는 값

    row_start=max(0,i-pick+1)#세로줄 터지기 시작하는 값
    row_end=min(n-1,i+pick-1)#세로줄 터지는 마지막 값
    col_start=max(0,j-pick+1)#가로줄 터지기 시작하는 값
    col_end=min(n-1,j+pick-1)#가로줄 터지는 마지막 값

    for r in range(row_start,row_end+1):
        tmp_grid[r][j]=0
    for c in range(col_start,col_end+1):
        tmp_grid[i][c]=0
    return tmp_grid

#tmp grid의 해당 줄에 대해서 중력 작용
def gravity():
    global tmp_grid #가로줄 중력범위 
    for y in range(n): #col_start,col_end+1
        none_zero=[] 
        for x in range(n-1,-1,-1):#맨 아랫줄부터 탐색 
            if tmp_grid[x][y]==0: 
                continue 
            else: 
                none_zero.append(tmp_grid[x][y]) 
        for x in range(n-len(none_zero)): 
            none_zero.append(0) 
        write_index=n-1 
        for x in range(n-1,-1,-1):#맨 아랫줄부터 값 넣기 
            tmp_grid[x][y]=none_zero[write_index] 
            write_index-=1 
    return tmp_grid

def count_set():
    global tmp_grid
    cnt=0
    for x in range(n):
        for y in range(n):
            if y<n-1 and tmp_grid[x][y]==tmp_grid[x][y+1] and tmp_grid[x][y]!=0 :#오른쪽 끝줄 제외, 오른쪽칸과 값이 같을때
                cnt+=1
            if x<n-1 and tmp_grid[x][y]==tmp_grid[x+1][y] and tmp_grid[x][y]!=0:#맨아래줄 제외, 아래칸과 값이 같을때
                cnt+=1
    return cnt

for i in range(n):
    for j in range(n):
        tmp_grid = [row[:] for row in grid]
        bomb(i,j)
        gravity()
        ans=max(ans,count_set())
print(ans)
