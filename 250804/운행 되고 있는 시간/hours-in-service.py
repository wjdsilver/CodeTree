n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]
ans=0

for i in range(n):
    time=[0]*1001
    for j in range(n):
        if i==j:
            continue
        for k in range(a[j],b[j]):
            time[k]=1
    cnt=0
    for l in time:
        if l!=0:
            cnt+=1
    ans=max(ans,cnt)
print(ans)
        