A=input()
arr=list(input())
for i in range(len(arr)):
    if arr[i]=="L":
        A = A[1:] + A[0]
    elif arr[i]=="R":
        A = A[-1] + A[:-1]
print(A)