arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

exist="NO"

for n in range (a,b+1):
    if n%c==0:
        exist="YES"

print(exist)
