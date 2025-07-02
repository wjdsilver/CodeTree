n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def seq(i):
    ans=0
    for a in range(queries[i][0]-1,queries[i][1]):
        ans+=arr[a]
    print(ans)


for i in range(m):
    seq(i)