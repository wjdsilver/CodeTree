arr=input().split()
h=int(arr[0])
w=int(arr[1])
b=10000*w//(h**2)
print(f"{b}")
if (b>=25):
    print("Obesity")