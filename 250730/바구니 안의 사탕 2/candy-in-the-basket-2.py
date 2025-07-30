N, K = map(int, input().split())
fin=0

bag=[0]*100
for i in range(N):
    candy,point=map(int,input().split())
    bag[point-1]+=candy

for i in range(100-K):
    ans=0
    for j in range(i-K,i+K+1):
        ans+=bag[j]
    fin=max(fin,ans)
print(fin)


