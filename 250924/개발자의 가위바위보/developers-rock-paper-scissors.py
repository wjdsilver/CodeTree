N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)
rcp,rpc,crp,cpr,pcr,prc=0,0,0,0,0,0

def RCP(x,y):
    global rcp,rpc,crp,cpr,pcr,prc
    if x==1 and y==2:
        rcp+=1
    elif x==2 and y==3:
        rcp+=1 
    elif x==3 and y==1:
        rcp+=1

def RPC(x,y):
    global rcp,rpc,crp,cpr,pcr,prc
    if x==1 and y==3:
        rpc+=1
    elif x==2 and y==1:
        rpc+=1 
    elif x==3 and y==2:
        rpc+=1

def CRP(x,y):
    global rcp,rpc,crp,cpr,pcr,prc
    if x==1 and y==3:
        crp+=1
    elif x==2 and y==1:
        crp+=1 
    elif x==3 and y==2:
        crp+=1

def CPR(x,y):
    global rcp,rpc,crp,cpr,pcr,prc
    if x==1 and y==2:
        cpr+=1
    elif x==2 and y==3:
        cpr+=1 
    elif x==3 and y==1:
        cpr+=1

def PCR(x,y):
    global rcp,rpc,crp,cpr,pcr,prc
    if x==1 and y==3:
        pcr+=1
    elif x==2 and y==1:
        pcr+=1 
    elif x==3 and y==2:
        pcr+=1

def PRC(x,y):
    global rcp,rpc,crp,cpr,pcr,prc
    if x==1 and y==2:
        prc+=1
    elif x==2 and y==3:
        prc+=1 
    elif x==3 and y==1:
        prc+=1


for i in range(N):
    if a[i]!=b[i]:
        RCP(a[i],b[i])
        RPC(a[i],b[i])
        CRP(a[i],b[i])
        CPR(a[i],b[i])
        PCR(a[i],b[i])
        PRC(a[i],b[i])
print(max(rcp,rpc,crp,cpr,pcr,prc))