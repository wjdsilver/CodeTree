n=int(input())

arr=[]

arr.append(1)
arr.append(n)

for i in range (2,10):
    arr.append(arr[i-2]+arr[i-1])
    if arr[i-2]+arr[i-1]>100:
        print(*arr)
        break
    else:
        pass