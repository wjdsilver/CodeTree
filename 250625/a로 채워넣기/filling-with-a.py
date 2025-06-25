A = input()
B = A[:1] + 'a' + A[2:]
C = B[:len(B)-2] + 'a' + B[len(B)-1:]
print(C)

