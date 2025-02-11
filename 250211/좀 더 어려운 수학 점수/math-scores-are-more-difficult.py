A=input().split()
B=input().split()
A_M=int(A[0])
A_E=int(A[1])
B_M=int(B[0])
B_E=int(B[1])

if A_M>B_M:
    print("A")
elif A_M==B_M and A_E>B_E:
    print("A")
else:
    print("B")