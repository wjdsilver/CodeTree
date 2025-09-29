n = int(input())
arr = list(map(int, input().split()))
arr.sort()
dis=[]
for i in range(1,n):
    dis.append(arr[n+i-1]-arr[i-1])
print(min(dis))