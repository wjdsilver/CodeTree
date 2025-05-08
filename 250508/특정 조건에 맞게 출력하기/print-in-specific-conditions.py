arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i]==0:
        arr.pop()
    else:
        pass

for j in range (i):
        if arr[j]%2==0:
            print(arr[j]//2,end=" ")
        elif arr[j]%2==1:
            print(arr[j]+3,end=" ")