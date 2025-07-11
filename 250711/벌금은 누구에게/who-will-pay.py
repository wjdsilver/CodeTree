N, M, K = map(int, input().split())
arr=[0]*(N+1)
ans=-1

for s in range(M):
    s=int(input())
    arr[s]+=1

    for i in range(1,N+1):
        if arr[i]==K:
            ans=i
            break
print(ans)

            

