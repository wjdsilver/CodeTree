def threes(n):
    result=False
    n=str(n)
    if "3" in n or "6" in n or "9" in n:
        result=True
    return result

a, b = map(int, input().split())
cnt=0
for i in range(a,b+1):
    if threes(i)==True or i%3==0:
        cnt+=1
print(cnt)