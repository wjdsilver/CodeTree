n = int(input())
arr = list(input().split())
cnt=0

for i in range(n-1):
    for j in range(i,n-1):
        if arr[j]>arr[j+1]:
            tmp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=tmp
            cnt+=1
print(cnt)
