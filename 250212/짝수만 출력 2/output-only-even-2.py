arr=input().split()
b=int(arr[0])
a=int(arr[1])
n=b
while (n>=a):
    if n%2==0:
        print(n,end=" ")
    n-=1