N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans=0

for i in range(N,0,-1):
    if B[i-1]-A[i-1]>=0:
        B[i-1]=B[i-1]-A[i-1]
        A[i-1]=0
    else: 
        A[i-1]=A[i-1]-B[i-1]
        B[i-1]=0

for j in range(0,N):
    while A[j]>0:
        for k in range(j,N):
            if B[k]>0:
                if B[k]>=A[j]:
                    ans+=(k-j)*A[j]
                    B[k]-=A[j]
                    A[j]=0
                if B[k]<A[j]:
                    ans+=(k-j)*B[k]
                    A[j]-=B[k]
                    B[k]=0
    else:
        continue
print(ans)