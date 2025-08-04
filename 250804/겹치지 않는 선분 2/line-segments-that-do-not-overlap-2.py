n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
cnt=0

for i in range(1,n-1):
    if lines[i-1][0]<lines[i][0] and lines[i-1][1]<lines[i][1]:
        if lines[i][0]<lines[i+1][0] and lines[i][1]<lines[i+1][1]:
            cnt+=1
if lines[0][0]<lines[1][0] and lines[0][1]<lines[1][1]:
    cnt+=1
if lines[n-2][0]<lines[n-1][0] and lines[n-2][1]<lines[n-1][1]:
    cnt+=1
print(cnt)