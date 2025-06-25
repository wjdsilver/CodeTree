A = input()
B = input()

while B in A:
        l=A.find(B)
        A=A[:l]+A[l+len(B):]
print(A)