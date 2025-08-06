X, Y = map(int, input().split())
ans=0

for i in range(X,Y+1):
    hap=0
    i=str(i)
    for j in range(len(i)):
        hap+=int(i[j])
    ans=max(ans,hap)
print(ans)