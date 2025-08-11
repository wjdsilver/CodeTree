import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans=sys.maxsize

for x in range(2,100,2):
    for y in range(2,100,2):
        cnt=[0]*5
        for i in range(n):
            if points[i][0]>=x and points[i][1]>=y:
                cnt[1]+=1
            elif points[i][0]<x and points[i][1]>=y:
                cnt[2]+=1
            elif points[i][0]<x and points[i][1]<y:
                cnt[3]+=1
            elif points[i][0]>=x and points[i][1]<y:
                cnt[4]+=1
        ans=min(ans,max(cnt))
print(ans)