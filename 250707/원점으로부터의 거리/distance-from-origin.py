n = int(input())
points = []


class Point():
    def __init__(self,x,y,n):
        self.x=x
        self.y=y
        self.n=n


for i in range(n):
    x,y=map(int, input().split())
    points.append(Point(x,y,i+1))

points.sort(key=lambda x:abs(x.x)+abs(x.y))
for elem in points:
    print(elem.n)