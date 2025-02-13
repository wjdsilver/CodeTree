arr=input().split()
a=int(arr[0])
b=int(arr[1])
result=a
for i in range(a,b+1):
    if result<=b:
        if result%2==1:
            print(result,end=" ")
            result*=2
        elif result%2==0:
            print(result,end=" ")
            result+=3
            
    