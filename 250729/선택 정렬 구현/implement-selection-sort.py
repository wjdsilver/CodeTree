n = int(input())
arr = list(map(int, input().split()))
tmp=0

def selection_sort(arr):
    l = len(arr)
  
    for i in range (l - 1):
        min=i
        for j in range (i+1,l):
            if arr[j] < arr[min]:
                min=j

        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp
    return arr

for i in selection_sort(arr):
    print(i,end=" ")
