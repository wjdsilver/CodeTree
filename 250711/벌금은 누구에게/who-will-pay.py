N, M, K = map(int, input().split())
arr=[0]*(N+1)
ans=-1

for _ in range(M):
    s=int(input())
    arr[s]+=1

    if arr[s] == K:
        print(s)
        break
else:
    print(-1)
            

