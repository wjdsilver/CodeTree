n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

vertical=[(-2,0),(-1,0),(0,0),(1,0),(2,0)]
cross=[(-1,0),(0,-1),(0,0),(0,1),(1,0)]
xshape=[(-1,-1),(-1,1),(0,0),(1,-1),(1,1)]
shapes=[vertical,cross,xshape]

bomb=[]

def inrange(x,y):
    return 0<=x<n and 0<=y<n

for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            bomb.append((i,j))

destroyed=[[False]* n for _ in range(n)]
answer=0

def bomb_explosion(idx,count):
    global answer
    #종료조건
    if idx==len(bomb):
        answer=max(answer,count)
        return
    x,y=bomb[idx]
    for shape in shapes:

        added = []

        # 현재 폭탄이 초토화시키는 칸 확인
        for dx, dy in shape:
            nx = x + dx
            ny = y + dy

            if inrange(nx, ny) and not destroyed[nx][ny]:
                destroyed[nx][ny] = True
                added.append((nx, ny))

        # 다음 폭탄으로
        bomb_explosion(idx + 1, count + len(added))

        # 원상복구
        for nx, ny in added:
            destroyed[nx][ny] = False

bomb_explosion(0,0) #시작인덱스,
print(answer)



