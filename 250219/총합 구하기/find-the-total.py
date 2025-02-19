arr=input().split()
a=int(arr[0])
b=int(arr[1])
int_sum=0
for i in range (a,b+1):
    if i%6==0 and i%8!=0:
        int_sum+=i
print(int_sum)
