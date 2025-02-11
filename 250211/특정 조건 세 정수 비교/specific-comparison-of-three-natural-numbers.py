arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if b<=c and b<=a:
    min= b
elif c<=a and c<=b:
    min=c
elif a<=b and a<=c:
    min= a 

print(int(min==a),end=" ")
print(int(a==b==c))