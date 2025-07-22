n, t = map(int, input().split())
r, c, d = input().split()
x, y = int(r), int(c)
x=x-1
y=y-1
leftT=t

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while leftT:
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
        
    else:
        move_dir = 3 - move_dir
    leftT -= 1
    
print(x+1,y+1)


