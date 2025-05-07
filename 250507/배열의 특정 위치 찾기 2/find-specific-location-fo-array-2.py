arr = list(map(int, input().split()))
filtered_arr1 = arr[::2]
sum_val1 = sum(filtered_arr1)

filtered_arr2 = arr[1::2]
sum_val2 = sum(filtered_arr2)
if sum_val1 <sum_val2:
    print(sum_val2-sum_val1)
else:
    print(sum_val1-sum_val2)