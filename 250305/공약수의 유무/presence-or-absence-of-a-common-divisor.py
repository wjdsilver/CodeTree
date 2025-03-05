arr=input().split()
a=int(arr[0])
b=int(arr[1])
common=0

for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        common=1
print(common)