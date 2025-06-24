A=input()
ans=""
for i in range(len(A)):
    if i%2==1:
        ans+=A[i]
print(ans[::-1])
