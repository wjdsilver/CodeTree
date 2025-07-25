N, T = map(int, input().split())
str = input()
grid = [list(map(int, input().split())) for _ in range(N)]

x,y=N//2,N//2
ans=grid[N//2][N//2]
move_dir = 3
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def inRange(r,c):
    return 0<=r<N and 0<=c<N

for w in str:
    if w=="L":
        move_dir = (move_dir + 3) % 4
    elif w=="R":
        move_dir = (move_dir + 1) % 4
    elif w=="F":
        nx,ny=x+dxs[move_dir],y+dys[move_dir]
        if inRange(nx,ny):
            x,y=nx,ny
            ans+=grid[x][y]
        
print(ans)

    

