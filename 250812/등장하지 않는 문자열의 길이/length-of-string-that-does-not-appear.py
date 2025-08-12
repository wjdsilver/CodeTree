N = int(input())
str = input()
ans=0

for i in range(N):
    s=False
    for j in range(N):
        if i+j+1>N:
            break
        sub=str[j:i+j+1] 
        if str.count(sub)==2:
            s=True
            ans=i+2
            break
    if s==False:
        break
print(ans)
