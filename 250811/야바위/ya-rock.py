n = int(input())
move = [tuple(map(int, input().split())) for _ in range(n)]
ans=0


def trick(peb):
    cnt=0
    for a,b,g in move:
        peb[a],peb[b]=peb[b],peb[a]
        if peb[g]==1:
            cnt+=1
    return cnt

for i in range(1,4):
    peb=[0]*4
    peb[i]=1
    ans=max(ans,trick(peb))
print(ans)