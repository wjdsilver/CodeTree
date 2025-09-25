n = int(input())
c = []
s = []
A,B=0,0
first=0 #공동이면 0 A면 1 B면2
change=0
cnt=0

for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

for i in range(n):
    if c[i]=="A":
        A+=s[i]
    else:
        B+=s[i]

    if A==B:
        change=0
    elif A>B:
        change=1
    elif A<B:
        change=2
    
    if first==change:
        continue
    else:
        first=change
        cnt+=1
print(cnt)


