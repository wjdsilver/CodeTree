A=list(input())
R=len(A)-1
for i in range(R):
    n=int(input())
    if n>len(A):
        A.pop(-1)
    else:
        A.pop(n)
    print("".join(A))

