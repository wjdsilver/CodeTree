n = int(input())
arr = list(map(int, input().split()))

for i in range(1,n+1,2):
    ans=arr[:i]
    ans.sort()
    print(ans[(i-1)//2],end=" ")