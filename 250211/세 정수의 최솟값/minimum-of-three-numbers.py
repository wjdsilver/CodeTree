arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a<=b and a<=c:
    min=a
elif b<=a and b<=c:
    min=b
elif c<=a and c<=b:
    min=c
print(min)