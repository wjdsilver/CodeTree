arr=input().split()
a=int(arr[0])
b=int(arr[1])
for i in range (1,10):
    for j in range (b,a-1,-2):
        print(f"{j} * {i} = {i * j}", end="")
        if a<j:
            print(" /", end=" ") 
    print()