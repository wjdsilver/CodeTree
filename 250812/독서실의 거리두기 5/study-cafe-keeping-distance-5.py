N = int(input())
seat = input()
fin=0

for i in range(len(seat)):
    seatIndex=[]
    if seat[i]=="1":
        continue
    else:
        newSeat=seat[:i]+"1"+seat[i+1:]
        for j in range(len(seat)):
            if newSeat[j]=="1":
                seatIndex.append(j)
        ans=N
        for k in range(len(seatIndex)-1):
            if seatIndex[k+1]-seatIndex[k]<ans:
                ans=seatIndex[k+1]-seatIndex[k]
    fin=max(fin,ans)
print(fin)

