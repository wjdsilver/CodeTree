n = int(input())
c = []
s = []
A,B,C=0,0,0
first=0 #공동이면 0 A면 1 B면2 C면3
change=0
cnt=0

for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

for i in range(n):
    if c[i]=="A":
        A+=s[i]
    elif c[i]=="B":
        B+=s[i]
    elif c[i]=="C":
        C+=s[i]

    if A==B==C:
        change=0
    elif A>B and A>C:
        change=1
    elif B>A and B>C:
        change=2
    elif C>A and C>B:
        change=3
    elif B>A and C>A and B==C:
        change=4
    elif A>B and C>B and A==C:
        change=5
    elif A>C and B>C and A==B:
        change=6
    else:
        change=7
    
    if first==change:
        continue
    else:
        first=change
        cnt+=1
print(cnt)
