arr=input().split()
a=int(arr[0])
b=int(arr[1])
prod=1
for i in range (1,b+1):
    if i%a==0:
        prod*=i
print(prod)