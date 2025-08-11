A, B, C = map(int, input().split())
ans=0

for i in range(C//A+1):
    for j in range(C//B+1):
        if A*i+B*j<C:
            ans=max(ans,A*i+B*j)

print(ans)