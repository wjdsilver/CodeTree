n, m, r, c = map(int, input().split())
directions = list(input().split())
r-=1
c-=1
LMROUD=[4,6,3,1,5,2]#왼,본인,오,마주본,위,아래

grid=[[0]*n for _ in range (n)]
grid[r][c] = LMROUD[1]

def move(x):
    global r,c,LMROUD
    if directions[x]=="L":
        LMROUD=[LMROUD[3]]+LMROUD[:3]+LMROUD[4:]
        c-=1
    elif directions[x]=="U":
        LMROUD=[LMROUD[0]]+[LMROUD[4]]+[LMROUD[2]]+[LMROUD[5]]+[LMROUD[3]]+[LMROUD[1]]
        r-=1
    elif directions[x]=="R":
        LMROUD=LMROUD[1:4]+[LMROUD[0]]+LMROUD[4:]
        c+=1
    elif directions[x]=="D":
        LMROUD=[LMROUD[0]]+[LMROUD[5]]+[LMROUD[2]]+[LMROUD[4]]+[LMROUD[1]]+[LMROUD[3]]
        r+=1
    return LMROUD

for i in range (m):#m번에 걸쳐서
    move(i)
    if 0 <= r < n and 0 <= c < n:
        grid[r][c] = LMROUD[1]

print(sum(sum(row) for row in grid))
