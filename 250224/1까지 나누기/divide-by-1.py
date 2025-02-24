n=int(input())
cnt=0
for i in range (1,n+1):
    n=n//i
    if n>1:
        cnt+=1
        continue
    elif n<=1:
        break
print(cnt+1)
