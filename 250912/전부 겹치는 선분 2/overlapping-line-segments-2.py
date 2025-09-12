n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

newX1=[]
newX2=[]

ans=False

for i in range(n):
    newX1=x1[:i]+x1[i+1:]
    newX2=x2[:i]+x2[i+1:]
    if max(newX1)<=min(newX2):
        ans=True

if ans==False:
    print("No")
else:
    print("Yes")