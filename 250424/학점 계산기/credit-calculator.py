n = int(input())
arr = list(map(float, input().split()))

sum_val = sum(arr[0:])

print(f"{sum_val/n:.1f}")
if sum_val/n>=4.0:
    print("Perfect")
elif 4.0>sum_val/n>=3.0:
    print("Good")
elif 3.0>sum_val/n:
    print("Poor")
