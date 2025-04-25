arr = list(map(int, input().split()))
temp = []

for i in arr:
    if i == 0:
        break
    temp.append(i)
    sum_val=sum(temp[0:])
    n=len(temp)
print(f"{sum_val} {sum_val/n:.1f}")
