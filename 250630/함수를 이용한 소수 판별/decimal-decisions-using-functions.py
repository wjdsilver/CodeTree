def prime(n):
    result=True
    for i in range (2,n):
        if n%i==0:
            result=False
            break
    return result


a, b = map(int, input().split())
ans=0
for i in range(a,b+1):
    if prime(i)==True:
        ans+=i
print(ans)