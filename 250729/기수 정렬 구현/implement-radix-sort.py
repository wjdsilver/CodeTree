n = int(input())
arr = list(map(int, input().split()))

def radix_sort(arr):
    max_num = max(arr)
    k = len(str(max_num))
    for pos in range(k):
        arr_new = [[]for _ in range (10)]
        for i in range(len(arr)):
            digit = (arr[i] // (10 ** pos)) % 10
            arr_new[digit].append(arr[i])

        store_arr = []
        for i in range(10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])
        arr = store_arr

    return arr

for i in radix_sort(arr):
    print(i,end=" ")