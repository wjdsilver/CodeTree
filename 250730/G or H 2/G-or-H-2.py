n = int(input())
arr=[0]*101
fin=0

for _ in range(n):
    spot,ppl=input().split()
    spot=int(spot)
    arr[spot]=ppl

for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]!=0 and arr[j]!=0:
            cntG=0
            cntH=0
            for k in range(i,j+1):
                if arr[k]=="G":
                    cntG+=1
                elif arr[k]=="H":
                    cntH+=1
            if cntG==cntH or cntG==0 or cntH==0:
                ans=j-i
                #print(j,i,ans)
                fin=max(fin,ans) 
print(fin)
            
