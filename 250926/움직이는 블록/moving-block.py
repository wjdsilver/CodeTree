n = int(input())
blocks = [int(input()) for _ in range(n)]
ans=0

for i in range(n):
    if blocks[i]>(sum(blocks)//n):
        ans+=blocks[i]-sum(blocks)//n
print(ans)