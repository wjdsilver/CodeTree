n=int(input())
ans=0
cnt=0

for _ in range(n):
    a=input()
    ans+=len(a)
    if a[0]=='a':
        cnt+=1
print(ans, cnt)