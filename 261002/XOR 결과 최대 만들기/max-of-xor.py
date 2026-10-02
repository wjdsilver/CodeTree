n, m = map(int, input().split()) #n개 정수중 m개를 뽑아서 xor
A = list(map(int, input().split()))
finalans=0

def maxXOR(idx,num,cnt):
    global finalans
    #종료조건
    if cnt==m:
        finalans=max(num,finalans)
        return 
    if idx==len(A):
        return
    maxXOR(idx+1,num,cnt)

    maxXOR(idx+1,num^A[idx],cnt+1)
maxXOR(0,0,0)
print(finalans)


