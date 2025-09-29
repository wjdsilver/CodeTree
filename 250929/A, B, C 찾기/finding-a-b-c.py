arr = list(map(int, input().split()))
arr.sort()
ABC=max(arr)
A=min(arr)
B=arr[1]
C=ABC-A-B
print(A,B,C)

