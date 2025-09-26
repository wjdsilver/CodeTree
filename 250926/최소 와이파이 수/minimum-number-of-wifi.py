n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt=0

while True:
    if 1 in arr:
        first=arr.index(1)
        for i in range(first,min(first+2*m+1,n)):
            if arr[i]==1:
                arr[i]=0
        cnt+=1
    else:
        break

print(cnt)