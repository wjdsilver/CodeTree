arr=input().split()
a=int(arr[0])
b=int(arr[1])
int_sum=0
for i in range (a,b+1):
    if i%5==0 or i%7==0:
        int_sum+=i
print(f"{int_sum} {int_sum/(b-a+1):.1f}")
