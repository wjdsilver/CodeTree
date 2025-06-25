A=input()
for i in range(len(A)-1):
    A=list(A)
    n=int(input())
    if n>len(A):
        A.pop(-1)
    else:
        A.pop(n)
    A="".join(A)
    print(A)

