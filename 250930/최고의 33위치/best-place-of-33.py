n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=0

for i in range(n-2):#좌상단
    for j in range(n-2):#좌상단
        cnt=0
        for k in range(3):
            for m in range(3):
                if grid[i+k][j+m]==1:
                    cnt+=1
        ans=max(ans,cnt)
print(ans)