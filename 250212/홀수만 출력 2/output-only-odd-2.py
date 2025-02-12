arr=input().split()
b=int(arr[0])
a=int(arr[1])

for i in range(b,a-1,-1):
    if i%2==1:
        print(i,end=" ")