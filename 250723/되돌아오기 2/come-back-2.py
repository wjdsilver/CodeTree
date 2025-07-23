import sys
arr=input()
N = len(arr)

t=0
ans=-1
x,y=0,0
move_dir = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = {
    'N': 0,
    'E': 1,
    'W': 2,
    'S': 3
}


for w in arr:
    if w=="L":
        move_dir = (move_dir + 4 - 1) % 4
        t+=1
    elif w=="R":
        move_dir = (move_dir + 1) % 4
        t+=1
    elif w=="F":
        x,y=x+dxs[move_dir],y+dys[move_dir]
        t+=1
        if x==0 and y==0:
            print(t)
            sys.exit()
            
        
print(-1)

    

