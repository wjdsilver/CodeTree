a = input()
na=""
ans=0
if a[1]=="0":
    na="11"+a[2:]
elif a[1]=="1":
    na="10"+a[2:]
ans = int(na, 2)
print(ans)