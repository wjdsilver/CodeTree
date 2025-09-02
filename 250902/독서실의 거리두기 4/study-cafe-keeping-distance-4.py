N = int(input())
seat = input()
fin=0

for i in range(N-1):
    nseat=list(seat)
    Nseat=[]
    for j in range(i,N):
        if seat[i]=="0" and seat[j]=="0":
            nseat[i]="1"
            nseat[j]="1"
            mini=N
            for n,elem in enumerate(nseat):
                if elem=="1":
                    Nseat.append(n)
                    
            for j in range(len(Nseat)-1):
                ans=Nseat[j+1]-Nseat[j]
                mini=min(ans,mini)
            fin=max(fin,mini)
print(fin)