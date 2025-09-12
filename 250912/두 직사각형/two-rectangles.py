x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

intersect=False

if a1<=x2 or b1<=y2:
    intersect=True
if x1<=a2 or y1<=b2:
    intersect=True
if intersect==True:
    print("overlapping")
else:
    print("nonoverlapping")