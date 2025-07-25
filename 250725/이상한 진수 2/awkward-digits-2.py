a = input()
na=""
ans=0
if a[1]=="0":
    na="11"+a[2:]
elif a[1]=="1":
    na="10"+a[2:]
for i in range(len(na)):
    na=int(na)
    ans+=na%10*(2**i)
    na=na//10
print(ans)