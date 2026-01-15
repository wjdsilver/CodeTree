n, m = map(int, input().split())
grid = [
    [[int(x)] for x in input().split()]
    for _ in range(n)
]#격자판 정보
move_nums = list(map(int, input().split()))#이동할 숫자

dxs=[-1,-1,-1,0,0,1,1,1]
dys=[-1,0,1,-1,1,-1,0,1]


#8방향으로 이동하기
def move8ways(r,c,x):
    br=r
    bc=c
    best=0
    for d in range(8):
        nr=r+dxs[d]
        nc=c+dys[d]
        #큰 값 가진 칸 찾기
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] and max(grid[nr][nc]) > best:
                br=nr
                bc=nc
                best=max(grid[nr][nc])
    idx = grid[r][c].index(x)
    moving = grid[r][c][idx:]
    grid[r][c] = grid[r][c][:idx]
    
    grid[br][bc]+=moving

    



for i in range(m):
    x = move_nums[i]
    moved = False
    for r in range(n):
        for c in range(n):
            if x in grid[r][c]:
                move8ways(r, c, x)
                moved = True
                break
        if moved:
            break

for i in range(n):
    for j in range(n):
        if grid[i][j]==[]:
            print("None")
        else:
            print(*grid[i][j][::-1])
