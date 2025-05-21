arr = list(map(int, input().split()))
count_arr = [0] * 10

for i in arr:
    if i == 0:
        break
    ten = i // 10
    count_arr[ten] += 1

for i in range(1, 10):
    print(f"{i} - {count_arr[i]}")



