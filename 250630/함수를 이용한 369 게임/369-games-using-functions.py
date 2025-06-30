def threes(n):
    result=False
    for i in range(1,7):
        if n%(10^i)==3 or n%(10^i)==6 or n%(10^i)==9:
            result=True
    return result

a, b = map(int, input().split())
cnt=0
for i in range(a,b+1):
    if threes(i)==True or i%3==0:
        cnt+=1
print(cnt)