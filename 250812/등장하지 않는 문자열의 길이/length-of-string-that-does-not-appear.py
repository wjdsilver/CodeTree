N = int(input())
str = input()
ans=0

for i in range(N//2+1):
    sub=str[:i+1] 
    if str.count(sub)==2:
        ans=i+2
    else:
        break
print(ans)