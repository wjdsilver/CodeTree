arr = list(map(int, input().split()))
count_arr = [0] * 11

for i in arr:
    if i == 0:
        break
    ten = i // 10
    count_arr[ten] += 1

for i in range(10,0,-1):
    print(f"{i}0 - {count_arr[i]}")



