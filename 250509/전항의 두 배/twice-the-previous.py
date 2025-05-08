arr = list(map(int, input().split()))

cnt=1
while cnt<9:
    cnt+=1
    arr.append(arr[cnt-1]+2*arr[cnt-2])
print(*arr)
    