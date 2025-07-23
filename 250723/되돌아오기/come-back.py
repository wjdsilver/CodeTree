import sys
N = int(input())

t=0
ans=-1
x,y=0,0

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'N': 0,
    'E': 1,
    'W': 2,
    'S': 3
}


for i in range(N):
    w,d=input().split()
    d=int(d)
    move_dir = mapper[w]
    for _ in range(d):
        x,y=x+dxs[move_dir],y+dys[move_dir]
        t+=1
        if x==0 and y==0:
            print(t)
            sys.exit()
            
        
print(-1)

    