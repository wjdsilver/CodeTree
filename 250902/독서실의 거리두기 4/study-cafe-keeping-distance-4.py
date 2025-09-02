N = int(input())
seat = input()
fin=0

for i in range(N-1):
    for j in range(i+1,N):
        nseat=list(seat)
        Nseat=[]
        if seat[i]=="0" and seat[j]=="0":
            nseat[i]="1"
            nseat[j]="1"
            mini=N
            for n,elem in enumerate(nseat):
                if elem=="1":
                    Nseat.append(n)
                    
            for x in range(len(Nseat)-1):
                ans=Nseat[x+1]-Nseat[x]
                mini=min(ans,mini)
            fin=max(fin,mini)
print(fin)