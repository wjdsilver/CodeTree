x1, x2, x3, x4 = map(int, input().split())

overlap=True

if x2<x3:
    overlap=False
if x4<x1:
    overlap=False
    
if overlap==True:
    print("intersecting")
else:
    print ("nonintersecting")
    