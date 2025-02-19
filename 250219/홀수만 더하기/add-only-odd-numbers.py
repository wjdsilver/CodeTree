n=int(input())
int_sum=0
for i in range(n):
    a=int(input())
    if a%2==1 and a%3==0:
        int_sum+=a
    else:
        pass
print(int_sum)
