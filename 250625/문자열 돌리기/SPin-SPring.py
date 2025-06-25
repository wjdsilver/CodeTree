A=input()
print(A)
for i in range(len(A)):
    A = A[-1] + A[:-1]
    print(A)
