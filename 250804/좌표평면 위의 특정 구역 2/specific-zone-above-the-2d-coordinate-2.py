import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
minbox=sys.maxsize

for i in range(n):
    nx=[]
    ny=[]
    for j in range(n):
        if j==i:
            continue
        nx.append(x[j])
        ny.append(y[j])
    box=(max(nx)-min(nx))*(max(ny)-min(ny))
    minbox=min(minbox,box)
        
print(minbox)