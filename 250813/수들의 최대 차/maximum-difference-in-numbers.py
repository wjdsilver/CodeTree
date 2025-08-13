N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
fin=0

arr.sort()
for i in range(N):
    cnt=0
    for j in range(N):
        if arr[i]<=arr[j]<=arr[i]+K:
            cnt+=1
    fin=max(fin,cnt)
print(fin)