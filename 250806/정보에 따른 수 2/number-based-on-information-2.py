import sys

T, a, b = map(int, input().split())
N = []
S = []

for _ in range(T):
    char, pos = input().split()
    if char=="N":
        N.append(int(pos))
    else:
        S.append(int(pos))

N.sort()
S.sort()
cnt=0

for i in range(a,b+1):
    d1=sys.maxsize
    d2=sys.maxsize
    for k in S:
        lS=abs(i-k)
        d1=min(d1,lS)
    for j in N:
        lN=abs(i-j)
        d2=min(d2,lN)
    if d1<=d2:
        cnt+=1
print(cnt)
