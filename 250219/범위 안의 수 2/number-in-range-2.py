int_sum=0
cnt=0
for i in range(10):
    n=int(input())
    if 0<=n and n<=200:
        int_sum+=n
        cnt+=1
print(f"{int_sum} {int_sum/cnt:.1f}")