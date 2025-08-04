K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
cnt=0

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        lineUp = True
        for k in range(K):
            rank = arr[k]
            if rank.index(a) > rank.index(b):
                lineUp = False
                break
        if lineUp:
            cnt += 1
print(cnt)
            
            