n = int(input())
arr = list(map(int, input().split()))
tmp=0

def bubble_sort(arr):
    l = len(arr)
  
    for i in range (l - 1):
        for j in range (l - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

for i in bubble_sort(arr):
    print(i,end=" ")