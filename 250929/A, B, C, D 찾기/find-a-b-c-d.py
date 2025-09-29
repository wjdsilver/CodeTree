arr = list(map(int, input().split()))

arr.sort()
A=arr[0]
B=arr[1]
C=arr[2]
ABCD=max(arr)
D=ABCD-A-B-C

print(A,B,C,D)