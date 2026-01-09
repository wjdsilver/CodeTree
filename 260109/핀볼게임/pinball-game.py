n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]#벽 방향 입력되어있음
ans=0

#U,R,D,L 순서로
dxs=[-1,0,1,0]
dys=[0,1,0,-1]

def inRange(x,y):
    return 0<=x<n and 0<=y<n

def move(x,y,d):
    #초기세팅
    ball_x=x
    ball_y=y
    time=1
    if d == "U": di = 0
    elif d == "R": di = 1
    elif d == "D": di = 2
    else: di = 3

    while True:
        # 현재 칸에서 방향 전환
        if grid[ball_x][ball_y] == 1:  # /
            if di == 0: di = 1
            elif di == 1: di = 0
            elif di == 2: di = 3
            elif di == 3: di = 2

        elif grid[ball_x][ball_y] == 2:  # \
            if di == 0: di = 3
            elif di == 3: di = 0
            elif di == 2: di = 1
            elif di == 1: di = 2
            
        ball_x+=dxs[di]
        ball_y+=dys[di]
        time+=1
        if not inRange(ball_x,ball_y):
            return time
        
    return time


for i in range(n):
    #맨 윗줄, 맨 오른줄, 맨아랫줄, 맨왼줄 각각 
    ans=max(ans,move(0,i,"D"))
    ans=max(ans,move(n-1,i,"U"))
    ans=max(ans,move(i,0,"R"))
    ans=max(ans,move(i,n-1,"L"))
    
print(ans)