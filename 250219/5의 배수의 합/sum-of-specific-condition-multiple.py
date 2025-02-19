arr=input().split()
a=int(arr[0])
b=int(arr[1])
int_sum=0
if a>b:
    a,b=b,a
for i in range (a,b+1):
    if i%5==0:
        int_sum+=i
print(int_sum)