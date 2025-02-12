arr=input().split()
a=int(arr[0])
b=int(arr[1])
if a>=b:
    for i in range (b-1,a):
        print(a,end=" ")
        a-=1
elif b>a:
    for i in range (a-1,b):
        print(b,end=" ")
        b-=1