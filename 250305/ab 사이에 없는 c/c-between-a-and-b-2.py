arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

NY="YES"
for i in range(a,b+1):
    if i%c==0:
        NY="NO"

print(NY)