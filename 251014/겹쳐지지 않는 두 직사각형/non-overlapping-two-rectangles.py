n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=-100

#사각형 내부점
def inSquare(x1,y1,x2,y2):
    square=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            square+=grid[i][j]
    return square

#사각형 겹치는지 
def overlap(x1, y1, x2, y2, a1, b1, a2, b2):
    return not (x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1)

#사각형1
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1,n):
            for y2 in range(y1,m):
                #사각형2
                for a1 in range(n):
                    for b1 in range(m):
                        for a2 in range(a1,n):
                            for b2 in range(b1,m):

                                if not overlap(x1, y1, x2, y2, a1, b1, a2, b2):
                                    ans=max(ans,inSquare(x1,y1,x2,y2)+inSquare(a1,b1,a2,b2))
print(ans)


