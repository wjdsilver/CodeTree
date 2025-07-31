N = int(input())
a, b, c = [], [], []
ans=0
arr=[]

for _ in range(N):
    num, c1, c2 = map(int, input().split())
    a.append(str(num))
    b.append(c1)
    c.append(c2)

for n in range(100,1000):
    #if n%10 != n//10%10 and n//10%10 != n//100 and n//100 != n%10 and n//10%10 != 0 and n//100 != 0:
    s = str(n)
    if '0' in s:
        continue
    if len(set(s)) == 3:
        arr.append(s)

for n in arr:
    ok=True
    for m in range(len(a)):
        cnt1=0
        cnt2=0
        for i in range(3):
            if n[i]==a[m][i]:
                cnt1+=1
            elif n[i] in a[m]:
                cnt2+=1
        if cnt1 != b[m] or cnt2 != c[m]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)


