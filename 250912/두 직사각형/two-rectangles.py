x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

intersect=True

if a1>x2:
    intersect=False
if x1>a2:
    intersect=False
if b2<y1:
    intersect=False
if y2<b1:
    intersect=False
    
if intersect==True:
    print("overlapping")
else:
    print("nonoverlapping")