n = int(input())
g=[0]*200001 #w면1 b면2 g면 3
w=[0]*200001
b=[0]*200001
cur=100000
wn,bn,gn=0,0,0

for _ in range(n):
    x, di = input().split()
    x=int(x)

    if di=="L":
        for j in range(cur-x+1,cur+1):
            if g[j]==3:
                continue
            else:
                if w[j]==0:
                    w[j]=1
                    g[j]=1
                elif w[j]==1:
                    if b[j]>=2:
                        g[j]=3
                    else:
                        w[j]=2
                        g[j]=1
        cur=cur-x+1
    elif di=="R":
        for j in range(cur,cur+x):
            if g[j]==3:
                continue
            else:
                if b[j]==0:
                    b[j]=1
                    g[j]=2
                elif b[j]==1:
                    if w[j]>=2:
                        g[j]=3
                    else:
                        b[j]=2
                        g[j]=2
        cur=cur+x-1

for i in range(2001):
    if g[i]==1:
        wn+=1
    elif g[i]==2:
        bn+=1
    elif g[i]==3:
        gn+=1
print(wn,bn,gn)
