A = input()
a1=A[0]
a2=A[1]
A=list(A)
for i in range(len(A)):
    if A[i]==a1:
        A[i]=a2
    elif A[i]==a2:
        A[i]=a1
print("".join(A))

