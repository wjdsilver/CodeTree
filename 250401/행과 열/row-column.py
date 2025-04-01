arr=input().split()
i=int(arr[0])
j=int(arr[1])

for a in range(1,i+1):
    for b in range(1,j+1):
        print(a*b,end=" ")
    print()