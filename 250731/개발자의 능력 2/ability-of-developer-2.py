import sys
arr = list(map(int, input().split()))
arr.sort()
ans=sys.maxsize

team1=arr[0]+arr[5]
for i in range(1,4):
    for j in range(i+1,5):
        team2=arr[i]+arr[j]
        team3=sum(arr)-team1-team2
        M=max(team1,team2,team3)
        m=min(team1,team2,team3)
        ans=min(M-m,ans)
print(ans)