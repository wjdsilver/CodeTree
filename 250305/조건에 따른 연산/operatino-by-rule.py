n=int(input())
cnt=0
while n<1000:
    if n%2==0:
        n=3*n+1
    elif n%2==1:
        n=2*n+2
    cnt+=1
print(cnt)