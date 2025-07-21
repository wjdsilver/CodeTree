x,y=0,0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
n = int(input())
for _ in range(n):
    w,d=input().split()
    d=int(d)
    
    if w == "W":
        x,y = x + dx[0]*d, y + dy[0]*d
    elif w == "S":
        x, y = x + dx[1]*d, y + dy[1]*d
    elif w == "N":
        x, y = x + dx[2]*d, y + dy[2]*d
    else:
        x, y = x + dx[3]*d, y + dy[3]*d

print(x,y)