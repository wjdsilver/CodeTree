A=list(input())
old=A[1]
new=A[0]

for i in range(len(A)):
    if A[i]==old:
        A[i]=new
print("".join(A))