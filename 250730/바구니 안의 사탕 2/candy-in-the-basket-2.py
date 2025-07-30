N, K = map(int, input().split())
fin=0

bag=[0]*101
for i in range(N):
    candy,point=map(int,input().split())
    bag[point]+=candy

for i in range(101):
    ans=0
    for j in range(i-K,i+K+1):
        if 0<=j<=100:
            ans+=bag[j]
    fin=max(fin,ans)
print(fin)


