A = input()
cnt=1
ans=""
for i in range (1,len(A)):
    if A[i]==A[i-1]:
        cnt+=1
    if A[i]!=A[i-1]:
        ans+=A[i-1]
        ans+=str(cnt)
        cnt=1
ans+=A[-1]
ans+=str(cnt)
print(len(ans))
print(ans)
