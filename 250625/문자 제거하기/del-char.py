A=list(input())
for i in range(len(A)-1):
    n=int(input())
    if n>len(A):
        A.pop(-1)
    else:
        A.pop(n)
    print("".join(A))

