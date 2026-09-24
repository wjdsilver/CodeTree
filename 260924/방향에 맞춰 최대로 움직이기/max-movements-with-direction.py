#각 칸은 1~칸갯수에 해당하는 숫자 그리고 8방향 중 하나
n = int(input()) #격자크기
num = [list(map(int, input().split())) for _ in range(n)] #각 칸에 들어간 값
dir = [list(map(int, input().split())) for _ in range(n)] #각 칸에 들어간 방향
move_dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] #방향 값 별로 이동 방향
r, c = map(int, input().split()) #시작 위치
r-=1
c-=1
count=0

def inrange(x,y):
    return 0<=x<n and 0<=y<n

def move(r,c):# 시작 위치 입력
    max_count = 0

    dr, dc = move_dir[dir[r][c]-1]

    for k in range(1, n):
        nr = r + dr * k
        nc = c + dc * k

        if not inrange(nr, nc):
            break

        if num[nr][nc] > num[r][c]:
            max_count = max(max_count, 1 + move(nr, nc))

    return max_count

print(move(r,c)) 