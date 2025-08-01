import sys

arr = list(map(int, input().split()))
ans=sys.maxsize

for i in arr:
    team1=i
    for j in range(4):
        for k in range(j+1,5):
            if arr[j]!=i and arr[k]!=i:
                team2=arr[j]+arr[k]
                team3=sum(arr)-team1-team2
                if team1!=team2 and team1!=team3 and team2!=team3:
                    M=max(team1,team2,team3)
                    m=min(team1,team2,team3)
                    ans=min(ans,M-m)
if ans<1000:
    print(ans)
else: 
    print(-1)
        