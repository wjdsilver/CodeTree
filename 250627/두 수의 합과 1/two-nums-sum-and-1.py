a,b=map(int,input().split())
ans=str(a+b)
cnt=0
for i in ans:
    if i=="1":
        cnt+=1
    else:
        continue
print(cnt)