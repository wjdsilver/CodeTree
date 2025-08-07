n = int(input())
h = [int(input()) for _ in range(n)]

ans=0
for i in range(1,max(h)):#해수면 높이
    cnt=1
    for j in range(1,len(h)):
        if h[j-1]-i<=0 and 0<h[j]-i:
            cnt+=1
        else:
            continue
    ans=max(ans,cnt)
print(ans)
            