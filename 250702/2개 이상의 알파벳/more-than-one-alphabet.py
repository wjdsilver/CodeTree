A = input()

def issame(A):
    for i in range(len(A)-1):
        if A[i]==A[i+1]:
            continue
        elif A[i]!=A[i+1]:
            return False
    return True
    

if issame(A)==True:
    print("No")
else:
    print("Yes")