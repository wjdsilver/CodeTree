n, m, p = map(int, input().split())
p=p-1
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]
ppl=[(0)for _ in range(n)]

for i in range(p,m):
    ppl[ord(c[i])-ord('A')]=1

for j in range(p):
    if u[j]==u[p]:
        ppl[ord(c[j])-ord('A')]=1

for k in range(n):
    if ppl.count(0)>=u[p]:
        if u[p]==0:
            break
        if ppl[k]==0:
            print(chr(k+ord("A")),end=" ")
