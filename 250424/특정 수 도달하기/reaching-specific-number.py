arr = list(map(int, input().split()))
n= len(arr)
sum_val=0
cnt=0

for i in range (n):
    if arr[i]<250:
        sum_val+=arr[i]
        cnt+=1
    elif arr[i]>=250:
        print(f"{sum_val} {sum_val/cnt:.1f}")
        break
