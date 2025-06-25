A, q = input().split()
q = int(q)
Q = [int(input()) for _ in range(q)]

for i in range(q):
    if Q[i]==1:
        A = A[1:] + A[0]
        print(A)
    elif Q[i]==2:
        A = A[-1] + A[:-1]
        print(A)
    elif Q[i]==3:
        A=A[::-1]
        print(A)

