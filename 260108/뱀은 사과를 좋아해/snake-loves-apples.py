n, m, k = map(int, input().split())

######## 인풋으로 입력 받은 것들 ########
r, c = [], []#사과의 위치
for _ in range(m):#사과의 위치
    ri, ci = map(int, input().split())
    r.append(ri)
    c.append(ci)
apples = set(zip(r, c))

d, p = [], []#방향, 거리 정보
for _ in range(k):#방향, 거리 정보
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))
######## 인풋으로 입력 받은 것들 ########
snake_x=[1]#뱀 몸 x좌표
snake_y=[1]#뱀 몸 y좌표

#뱀이 격자 벗어났을때
def inRange(x,y):
    return 1<=x<=n and 1<=y<=n

def dup(x,y):
    return (x, y) in zip(snake_x, snake_y)

def move(i):
    global time,head_x,head_y,snake_x, snake_y
    
    for _ in range(p[i]):
        #머리
        if d[i] == "U":
            head_x -= 1
        elif d[i] == "D":
            head_x += 1
        elif d[i] == "L":
            head_y -= 1
        elif d[i] == "R":
            head_y += 1
        time+=1
        if not inRange(head_x,head_y):
            return False

        #꼬리
        if (head_x, head_y) in apples:
            apples.remove((head_x, head_y))
        else:
            snake_x=snake_x[1:] 
            snake_y=snake_y[1:]
        if dup(head_x,head_y):
            return False
        snake_x.append(head_x)
        snake_y.append(head_y)

    return True

time=0
head_x,head_y=1,1#뱀 머리 좌표

for i in range (k):
    if not move(i):
        break
print(time)