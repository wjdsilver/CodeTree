n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
ans=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if x[i]==x[j] or x[j]==x[k] or x[k]==x[i]:
                if y[i]==y[j] or y[j]==y[k] or y[k]==y[i]:
                    box=(max(x[i],x[j],x[k])-min(x[i],x[j],x[k]))*(max(y[i],y[j],y[k])-min(y[i],y[j],y[k]))
                    ans=max(box,ans)
if ans!=0:
    print(ans)
else:
    print(0)