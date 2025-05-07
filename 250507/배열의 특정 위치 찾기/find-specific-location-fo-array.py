arr = list(map(int, input().split()))
filtered_arr2 = arr[1::2]
sum_val2 = sum(filtered_arr2)

filtered_arr3 = arr[2::3]
sum_val3 = sum(filtered_arr3)
cnt=len(filtered_arr3)
print(f"{sum_val2} {sum_val3/cnt:.1f}")

